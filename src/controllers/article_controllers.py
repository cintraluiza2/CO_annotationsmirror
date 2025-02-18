from unidecode import unidecode
import re

from ..data.database import get_article, update_article

def regex_search(text:str, regex_terms:list):
    # Remoção de acentos
    text = unidecode(text)

    matches = []
    for regex_term in regex_terms:
        match = re.compile(regex_term, re.IGNORECASE).findall(text)
        matches.append(match[0])

    return matches

def update_article_on_db(_id: str, update: dict):
    update["manual_relevance_class"] = {
        "Sim": 1,
        "Não": 0,
        "Dúvida": 2,
    }[update["manual_relevance_class"]]
    
    print(_id)
    print(update)