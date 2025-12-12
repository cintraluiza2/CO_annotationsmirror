from unidecode import unidecode
from datetime import datetime
from bson import ObjectId
import pandas as pd
import re

from ..data import database as db
from ..settings import (
    DRUGS_DATA_MAPPING,
    OTHER_DRUGS_DATA_MAPPING,
    GUNS_DATA_MAPPING,
    ACTORS_DATA_MAPPING
)

def regex_search(text:str, regex_terms:list):
    # Remoção de acentos
    text = unidecode(text)

    matches = []
    for regex_term in regex_terms:
        match = re.compile(regex_term, re.IGNORECASE).findall(text)
        if match: # Se encontrar o termo no texto
            matches.append(match[0])

    return matches

def update_article_on_db(_id: str, update: dict):
    # Traduzindo o campo de relevância manual
    if update.get("manual_relevance_class"):
        update["manual_relevance_class"] = {
            "Sim": 1,
            "Não": 0,
            "Dúvida": 2,
        }[update["manual_relevance_class"]]

    # Traduzindo o país
    if update.get("country"):
        update["country"] = db.domain_translation(column_name="country", description=update["country"])

    # Traduzindo o campo de conflito
    if update.get("conflict"):
        update["conflict"] = db.domain_translation(column_name="conflict", description=update["conflict"])

    # Traduzindo o campo de tipo de droga
    drugs = []
    drugs_df = update.get("drugs", pd.DataFrame())
    if not drugs_df.empty and all(col in drugs_df.columns for col in ["Tipo de droga", "Quantidade", "Métrica"]):
        for _, row in drugs_df.iterrows():
            drug_type = str(row["Tipo de droga"]).strip()
            if drug_type and not drug_type.isspace() and drug_type != "nan":
                drugs.append({
                    "type": "fixed_field",
                    "drug_type": drug_type,
                    "amount": row["Quantidade"],
                    "metric": row["Métrica"],
                })
    
    other_drugs_df = update.get("other_drugs", pd.DataFrame())
    if not other_drugs_df.empty and all(col in other_drugs_df.columns for col in ["Outro tipo de droga", "Quantidade", "Métrica"]):
        for _, row in other_drugs_df.iterrows():
            drug_type = str(row["Outro tipo de droga"]).strip()
            if drug_type and not drug_type.isspace() and drug_type != "nan":
                drugs.append({
                    "type": "free_field",
                    "drug_type": drug_type,
                    "amount": row["Quantidade"],
                    "metric": row["Métrica"],
                })
    
    if "other_drugs" in update:
        del update["other_drugs"]
    update["drugs"] = drugs

    # Traduzindo o campo de tipo de arma
    guns = []
    guns_df = update.get("guns", pd.DataFrame())
    if not guns_df.empty and all(col in guns_df.columns for col in ["Tipo de arma", "Quantidade"]):
        for _, row in guns_df.iterrows():
            gun_type = str(row["Tipo de arma"]).strip()
            if gun_type and not gun_type.isspace() and gun_type != "nan":
                guns.append({
                    "gun_type": gun_type,
                    "quantity": row["Quantidade"],
                })
    update["guns"] = guns

    # Traduzindo o campo de atores
    actors = []
    actors_df = update.get("actors", pd.DataFrame())
    if not actors_df.empty and all(col in actors_df.columns for col in ["Ator 1", "Ator 2", "Relação"]):
        for _, row in actors_df.iterrows():
            relationship = str(row["Relação"]).strip()
            if relationship and not relationship.isspace() and relationship != "nan":
                actors.append({
                    "actor 1": row["Ator 1"],
                    "actor 2": row["Ator 2"],
                    "relationship": db.domain_translation(column_name="actors_relationship", description=relationship),
                })
    update["actors"] = actors

    # Traduzindo o campo de artigos do mesmo evento
    same_event_article_ids = []
    same_event_df = update.get("same_event", pd.DataFrame())
    if not same_event_df.empty and all(col in same_event_df.columns for col in ["ID da notícia"]):
        for _, row in same_event_df.iterrows():
            article_id = row["ID da notícia"]
            if pd.notna(article_id) and article_id:
                same_event_article_ids.append(int(article_id))
    update["same_event_articles_id"] = same_event_article_ids
    del update["same_event"]
    # Validação dos IDs inseridos
    if same_event_article_ids and not db.articles_exist(same_event_article_ids):
        return 0, f"Os dados não foram salvos. Pelo menos um dos IDs de notícias sobre o mesmo evento não existe."

    # Traduzindo o campo de data do evento
    if update.get("event_date"):
        update["event_date"] = datetime.combine(update["event_date"], datetime.min.time())

    # Traduzindo o campo de validação
    validated_value = update.get("validated", 0)
    if isinstance(validated_value, str):
        update["validated"] = {"Não": 0, "Sim": 1}.get(validated_value, 0)
    else:
        update["validated"] = int(validated_value) if validated_value is not None else 0
        
    db.update_article(ObjectId(_id), update) # 9805

    return 1, "Sucesso"

def get_article(_id: str):
    article = db.get_article(_id)

    # Formatação da data de publicação
    if article.get("publication_date"):
        article["publication_date"] = article["publication_date"].strftime("%d/%m/%Y")

    # Formação das drogas do campo do campo livre, isto é, onde "droga" e "métrica" era digitados
    free_type_drugs = [drug for drug in article.get("drugs", []) if drug.get("type", "") == "free_field"]
    if free_type_drugs:
        article["other_drugs"] = pd.DataFrame(
            free_type_drugs
        ).rename(axis=1, mapper=OTHER_DRUGS_DATA_MAPPING).drop("type", axis=1)
    else:
        article["other_drugs"] = pd.DataFrame(columns=OTHER_DRUGS_DATA_MAPPING.values())

    # Formação das drogas do campo do campo fixo, isto é, onde "droga" e "métrica" era selecionados
    fixed_type_drugs = [drug for drug in article.get("drugs", []) if drug.get("type", "") == "fixed_field"]
    if fixed_type_drugs:
        article["drugs"] = pd.DataFrame(
            fixed_type_drugs
        ).rename(axis=1, mapper=DRUGS_DATA_MAPPING).drop("type", axis=1)
    else:
        article["drugs"] = pd.DataFrame(columns=DRUGS_DATA_MAPPING.values())

    # Formação das armas
    if article.get("guns"):
        article["guns"] = pd.DataFrame(
            article.get("guns")
        ).rename(axis=1, mapper=GUNS_DATA_MAPPING)
    else:
        article["guns"] = pd.DataFrame(columns=GUNS_DATA_MAPPING.values())

    # Formatação dos atores e suas relações
    if article.get("actors"):
        relationships = []
        for relationship in article.get("actors"):
            relationships.append(relationship)
            relationships[-1]["relationship"] = db.domain_translation("actors_relationship", value=relationship["relationship"])
        article["actors"] = pd.DataFrame(
            relationships
        ).rename(axis=1, mapper=ACTORS_DATA_MAPPING)
    else:
        article["actors"] = pd.DataFrame(columns=ACTORS_DATA_MAPPING.values())

    if article.get("same_event_articles_id"):
        article["same_event_articles_id"] = pd.DataFrame(data=article.get("same_event_articles_id"), columns=["ID da notícia"])
    else:
        article["same_event_articles_id"] = pd.DataFrame(columns=["ID da notícia"])

    return article

def get_countries():
    return db.get_countries()

def domain_translation(column_name, value=None, description=None):
    return db.domain_translation(column_name, value, description)