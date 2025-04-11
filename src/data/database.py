from sshtunnel import SSHTunnelForwarder
from pymongo import MongoClient
from bson import ObjectId
import pandas as pd
import threading
import pymongo
import socket
import yaml
import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
logging.getLogger("watchdog.observers.inotify_buffer").setLevel(logging.WARNING)
logging.getLogger("paramiko").setLevel(logging.WARNING)
logging.getLogger("pymongo").setLevel(logging.WARNING)

server = None # Servidor do banco
db_client = None # Cliente do banco
tunnel_timer = None # Timmer de controle de abertura do banco

# Leitura do arquivo de credenciais
configs_file = open('config.yml', 'r')
configs = yaml.safe_load(configs_file)
configs_file.close()

def is_port_open(host="localhost", port=27018, timeout=1):
    """
    Verifica se a porta está aberta no servidor especificado.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        return s.connect_ex((host, port)) == 0

def is_tunnel_open() -> bool:
    """
    Verifica se há conexão com um servidor.
    """
    return (not server is None) and server.is_active

def open_ssh_tunnel(timeout_minutes=10) -> MongoClient:
    """
    Abre o túnel SSH onde está o MongoDB e retorna o cliente do banco.
    Se não houver novas tentativas de abertua do túnel, este é fechado em `timeout_minutes`.
    """
    global server, db_client, tunnel_timer

    if not is_tunnel_open():
        if not is_port_open():
            server = SSHTunnelForwarder(
                (configs["lamcad"]["server_ip"], configs["lamcad"]["server_port"]),
                ssh_username=configs["lamcad"]["ssh_username"],
                ssh_password=configs['lamcad']['ssh_password'],
                local_bind_address=("localhost", 27018),
                remote_bind_address=("127.0.0.1", 27017),
            )
            server.start() # Abrindo o túnel SSH
            logging.info("SSH Tunnel opened.")
        db_client = pymongo.MongoClient(configs["mongodb_lamcad"]["uri"]) # Criando um cliente do banco

    # Reiniciando o timer
    if tunnel_timer is not None:
        tunnel_timer.cancel()
    tunnel_timer = threading.Timer(timeout_minutes * 60, close_ssh_tunnel)
    tunnel_timer.start()

    return db_client

def close_ssh_tunnel():
    """
    Encerra a conexão SSH.
    """
    global server, db_client, tunnel_timer

    if server is not None:
        server.stop()
        server = None
        logging.info("SSH Tunnel closed.")

    if db_client is not None:
        db_client.close()
        db_client = None
    
    if tunnel_timer is not None:
        tunnel_timer.cancel()
        tunnel_timer = None

def get_newspapers():
    """
    Retorna os valores únicos de jornais presentes nas notícias.
    """
    db_client = open_ssh_tunnel()
    collection = db_client["couser"]["newsData"]
    newspaper = collection.distinct("newspaper")
    return newspaper
    
def get_article(_id: str):
    """
    Retorna os dados do artigo especificado.
    """
    db_client = open_ssh_tunnel()
    collection = db_client["couser"]["newsData"]

    object_id = ObjectId(_id)

    article = collection.find_one({"_id": object_id})

    return article

def update_article(_id: ObjectId, update: dict):
    """
    Atualiza os dados do artigo especificado, substituindo o objeto do banco por `update`.
    """
    db_client = open_ssh_tunnel()
    collection = db_client["couser"]["newsData"]
    collection.update_one({"_id": _id}, {"$set": update})

def get_best_classification_model():
    """
    Retorna o objeto que representa o pipeline de melhor acurácia
    na classificação de notícias. 
    """
    db_client = open_ssh_tunnel()
    collection = db_client["couser"]["classification_pipelines"]

    best_model = collection.find_one({}, sort=[("score", -1)])

    return best_model

def get_articles(filters: dict, as_df=True, page=1, items_per_page=20, sort="publication_date", sort_type=1):
    """
    Retorna os artigos a partir das especificações parametrizadas. Pode ser aplicada paginação com os parâmetros
    `page` e `items_per_page`.
    """
    db_client = open_ssh_tunnel()
    collection = db_client["couser"]["newsData"]

    pipeline = [] # Onde a query é descrita

    # Formatando a busca por título, se especificada uma string de título
    if filters.get('title'):
        pipeline.append({'$match': {"title": { "$regex": filters.get('title'), "$options": "i" }}})
    else:
        pipeline.append({"$match": {}})
    filters.pop("title", None)

    # Aplicando os demais filtros especificados em `filters`
    for key, value in filters.items():
        pipeline[0]["$match"].update({key: value})

    # Criando a projeção, isto é, quais dados devem ser retornados
    pipeline.append({
        '$project': {
            "_id": 1,
            "id_event": 1,
            "publication_date": 1,
            "newspaper": 1,
            "title": 1,
            "manual_relevance_class": 1,
            "automatic_relevance_class": 1,
            "automatic_relevance_pipeline_confidence": 1,
            "validated": 1,
        }
    })

    # Cálculo da notícia de início por paginação
    skip = (page-1) * items_per_page

    # Contagem de resultados
    pipeline_with_count = pipeline + [{'$count': 'total_count'}]
    count_result = collection.aggregate(pipeline_with_count)
    total_count = next(count_result, {}).get('total_count', 0)

    # Conversão do id da notícia em string
    pipeline.append({
        '$addFields': {
        '_id': {'$toString': '$_id'}
        }
    })
    pipeline.append({"$sort": {sort: sort_type, "_id": 1}})
    pipeline.append({"$skip": skip})
    pipeline.append({"$limit": items_per_page})

    # Requisitando os dados
    cursor = collection.aggregate(pipeline)
    articles = list(cursor)

    if as_df: # Se a resposta tiver que ser um pd.DataFrame
        df = pd.DataFrame(articles)
        
        # Preenchimento de colunas que podem não existir para as notícias retornadas
        if not "manual_relevance_class" in df.columns:
            df["manual_relevance_class"] = None
        if not "automatic_relevance_class" in df.columns:
            df["automatic_relevance_class"] = None
        if not "automatic_relevance_pipeline_confidence" in df.columns:
            df["automatic_relevance_pipeline_confidence"] = None

        # Preenchimento da coluna "validated" para quando não existir o atributo nos objetos
        if not "validated" in df.columns:
            df["validated"] = 0
        else:
            for i, row in df.iterrows():
                if pd.isna(row.get("validated", pd.NA)):
                    df.at[i, "validated"] = 0

        return df, total_count
    else:
        return articles, total_count
    
def count_articles():
    """
    Conta o número de artigos presentes no banco de dados.
    """
    db_client = open_ssh_tunnel()
    collection = db_client["couser"]["newsData"]
    count = collection.count_documents({})
    return count

def count_manual_classifications(values: list[int]):
    """
    Conta o número de artigos classificados manualmente.
    """
    db_client = open_ssh_tunnel()
    collection = db_client["couser"]["newsData"]
    count = collection.count_documents({"manual_relevance_class": {"$in": values}})
    return count

def count_automatic_classifications(values: list[int]):
    """
    Conta o número de artigos classificados automaticamente.
    """
    db_client = open_ssh_tunnel()
    collection = db_client["couser"]["newsData"]
    count = collection.count_documents({"automatic_relevance_class": {"$in": values}})
    return count

def count_manual_and_automatic_classifications(manual_values: list[int], automatic_values: list[int]):
    """
    Conta o número de artigos classificados manualmente e automaticamente.
    """
    db_client = open_ssh_tunnel()
    collection = db_client["couser"]["newsData"]
    count = collection.count_documents({
        "manual_relevance_class": {"$in": manual_values},
        "automatic_relevance_class": {"$in": automatic_values}
    })
    return count

def domain_translation(column_name, value=None, description=None):
    """
    Realiza a tradução de "valor <-> descrição" a partir das definições
    de domínio do banco.
    """
    db_client = open_ssh_tunnel()
    collection = db_client["couser"]["domain"]
    filter_ = {"column_name": column_name}
    
    # Verificando se foi informado `value` ou `description`
    if not value is None:
        filter_["value"] = value
    elif not description is None:
        filter_["description"] = description
    
    # Requisitando o banco para traduzir
    result = collection.find_one(filter_)
    if not value is None:
        return result.get("description")
    else:
        return result.get("value")
    
def get_countries():
    """
    Retorna os países definidos no domínio do banco de dados.
    """
    db_client = open_ssh_tunnel()
    collection = db_client["couser"]["domain"]
    filter_ = {"column_name": "country"}
    result = collection.find(filter_).sort("value", 1)
    return result

def articles_exist(id_events):
    """
    Verifica se um artigo existe a partir de um `id_event`. Se existir,
    o `_id` do artigo é retornado.
    """
    db_client = open_ssh_tunnel()
    collection = db_client["couser"]["newsData"]

    result = collection.find({"id_event": {"$in": id_events}}, {"_id": 1})

    return len(list(result)) == len(id_events)
