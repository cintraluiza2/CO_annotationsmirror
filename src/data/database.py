from sshtunnel import open_tunnel, SSHTunnelForwarder
from pymongo import MongoClient, DESCENDING
from bson import ObjectId
import pandas as pd
import threading
import time
import pymongo
import socket
import yaml
import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
logging.getLogger("watchdog.observers.inotify_buffer").setLevel(logging.WARNING)
logging.getLogger("paramiko").setLevel(logging.WARNING)
logging.getLogger("pymongo").setLevel(logging.WARNING)

server = None
db_client = None
tunnel_timer = None

# Leitura do arquivo de credenciais
configs_file = open('config.yml', 'r')
configs = yaml.safe_load(configs_file)
configs_file.close()

def is_port_open(host="localhost", port=27018, timeout=1):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        return s.connect_ex((host, port)) == 0

def is_tunnel_open() -> bool:
    """
    Verifica se há conexão com o servidor.
    """
    return (not server is None) and server.is_active

def open_ssh_tunnel(timeout_minutes=10) -> MongoClient:
    """
    Abre o túnel SSH onde está o MongoDB e retorna o cliente do banco.
    Se não houver novas interações, o túnel é fechado em `timeout_minutes`.
    """
    global server, db_client, tunnel_timer

    if not is_tunnel_open():
        print(is_port_open)
        if not is_port_open():
            server = SSHTunnelForwarder(
                ("200.137.215.38", 42112),
                ssh_username="couser",
                ssh_password=configs['lamcad']['ssh_password'],
                local_bind_address=("localhost", 27018),
                remote_bind_address=("127.0.0.1", 27017),
            )
            server.start()
            logging.info("SSH Tunnel opened.")
        db_client = pymongo.MongoClient(configs["mongodb_lamcad"]["uri"])

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
    # if not server is None:
    #     server.close()
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
    """Get list of available newspapers from database"""
    db_client = open_ssh_tunnel()
    collection = db_client["couser"]["newsData"]
    newspaper = collection.distinct("newspaper")
    return newspaper

def row_color(row):
    if row['manual_relevance_class'] == 0:
        return ['background-color: red'] * len(row)
    if row['manual_relevance_class'] == 1:
        return ['background-color: lightgreen'] * len(row)
    else:
        return [''] * len(row)
    
def get_article(_id: str):
    db_client = open_ssh_tunnel()
    collection = db_client["couser"]["newsData"]

    object_id = ObjectId(_id)

    article = collection.find_one({"_id": object_id})

    return article

def update_article(_id: ObjectId, update: dict):
    db_client = open_ssh_tunnel()
    collection = db_client["couser"]["newsData"]
    collection.update_one({"_id": _id}, update)

def get_best_classification_model():
    db_client = open_ssh_tunnel()
    collection = db_client["couser"]["classification_pipelines"]

    best_model = collection.find_one({}, sort=[("score", -1)])

    return best_model

def get_articles(filters: dict, as_df=True, page=1, items_per_page=20, sort="publication_date", sort_type=1):
    db_client = open_ssh_tunnel()
    collection = db_client["couser"]["newsData"]

    pipeline = []

    if filters.get('title'):
        pipeline.append({'$match': {"title": { "$regex": filters.get('title'), "$options": "i" }}})
    else:
        pipeline.append({"$match": {}})
    filters.pop("title", None)

    for key, value in filters.items():
        pipeline[0]["$match"].update({key: value})

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

    logging.debug(f"Pipeline query: {pipeline}")

    cursor = collection.aggregate(pipeline)
    
    articles = list(cursor)

    if as_df:
        df = pd.DataFrame(articles)
        
        # Preenchimento de colunas que podem não existir para as notícias retornadas
        if not "manual_relevance_class" in df.columns:
            df["manual_relevance_class"] = None
        if not "automatic_relevance_class" in df.columns:
            df["automatic_relevance_class"] = None
        if not "automatic_relevance_pipeline_confidence" in df.columns:
            df["automatic_relevance_pipeline_confidence"] = None

        # df['automatic_relevance_pipeline_confidence'] = df['automatic_relevance_pipeline_confidence'].apply(
        #     lambda x: x*100 if not x is None else None)
        return df, total_count
    else:
        return articles, total_count