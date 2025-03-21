from unidecode import unidecode
from datetime import datetime
from bson import ObjectId
import re

from ..data.database import get_article, update_article, domain_translation

def regex_search(text:str, regex_terms:list):
    # Remoção de acentos
    text = unidecode(text)

    matches = []
    for regex_term in regex_terms:
        match = re.compile(regex_term, re.IGNORECASE).findall(text)
        matches.append(match[0])

    return matches

def update_article_on_db(_id: str, update: dict):
    # print(update)

    # Traduzindo o campo de relevância manual
    if update.get("manual_relevance_class"):
        update["manual_relevance_class"] = {
            "Sim": 1,
            "Não": 0,
            "Dúvida": 2,
        }[update["manual_relevance_class"]]
    
    # Traduzindo o campo de conflito
    if update.get("conflict"):
        update["conflict"] = domain_translation(column_name="conflict", description=update["conflict"])

    # Traduzindo o campo de tipo de droga
    drugs = []
    for _, row in update.get("drugs").iterrows():
        if not row["Tipo de droga"].isspace():
            drugs.append({
                "drug_type": row["Tipo de droga"],
                "amount": row["Quantidade"],
                "metric": row["Métrica"],
            })
    for _, row in update.get("other_drugs").iterrows():
        if not row["Outro tipo de droga"].isspace():
            drugs.append({
                "drug_type": row["Outro tipo de droga"],
                "quantity": row["Quantidade"],
                "metric": row["Métrica"],
            })
    del update["other_drugs"]
    update["drugs"] = drugs

    # Traduzindo o campo de tipo de arma
    guns = []
    for _, row in update.get("guns").iterrows():
        if not row["Tipo de arma"].isspace():
            drugs.append({
                "gun_type": row["Tipo de arma"],
                "quantity": row["Quantidade"],
            })
    update["guns"] = guns

    # Traduzindo o campo de atores
    actors = []
    for _, row in update.get("actors").iterrows():
        if not row["Relação"].isspace():
            actors.append({
                "actor 1": row["Ator 1"],
                "actor 2": row["Ator 2"],
                "relationship": domain_translation(column_name="actors_relationship", description=row["Relação"]),
            })
    update["actors"] = actors

    # Traduzindo o campo de artigos do mesmo evento
    same_event_article_ids = []
    for _, row in update.get("same_event").iterrows():
        if row["ID da notícia"]:
            same_event_article_ids.append(row["ID da notícia"])
    update["same_event_articles_id"] = same_event_article_ids
    del update["same_event"]

    # Traduzindo o campo de data do evento
    if update.get("event_date"):
        update["event_date"] = datetime.combine(update["event_date"], datetime.min.time())

    print(update)

    update_article(ObjectId(_id), update) # 9805