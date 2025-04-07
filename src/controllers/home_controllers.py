from pymongo.errors import ServerSelectionTimeoutError
from datetime import datetime
import numpy as np

from ..data import database as db
from ..settings import (
    CONFIDENCE_SCALE,
    DEFAULT_SORTING_FIELD,
    ITEMS_PER_PAGE,
    FIELDS_MAPPING,
    INVERSE_FIELDS_MAPPING
)

def stylize_relevance_value(col):
    """
    Recebe uma coluna de pd.DataFrame e adiciona `background-color` às células a depender do valor de cada uma.
    - Se o valor for 0: vermelho.
    - Se o valor for 1: verde.
    - Demais valores: sem alteração.
    """
    style = []
    for value in col:
        if value == "Irrelevante":
            style.append('background-color: #ed685f')
        elif value == "Relevante":
            style.append('background-color: #5bb55b')
        else:
            style.append('')
    return style

def stylize_confidence_value(col):
    colors = []
    for value in col:
        if "%" in value:
            scale_index = (int(value.split("%")[0]) - 50) // 5
            style = f"background-color: {CONFIDENCE_SCALE[scale_index]};"
            if scale_index >= 4:
                style += "color: #dbdbdb;"
            else:
                style += "color: #2e2e2e;"
            colors.append(style)
        else:
            colors.append("")
    return colors

def get_articles_dataframe(filters, page=1, sort=DEFAULT_SORTING_FIELD, sort_type=-1):
    """
    Retorna o dataframe de notícias a ser exibido.
    """
    # Formatação da relevância manual
    if not filters.get("manual_relevance") == "Todas":
        if filters.get("manual_relevance") == "Relevantes":
            filters.update({"manual_relevance_class": 1})
        elif filters.get("manual_relevance") == "Irrelevantes":
            filters.update({"manual_relevance_class": 0})
        elif filters.get("manual_relevance") == "Dúvida":
            filters.update({"manual_relevance_class": 2})
        else: # Sem anotação
            filters.update(
                {"$or": [
                    {"manual_relevance_class": None},  # Field is None
                    {"manual_relevance_class": {"$exists": False}}]  # Field does not exist
                })
    filters.pop("manual_relevance", None)

    # Formatação da relevância automática
    if not filters.get("automatic_relevance") == "Todas":
        if filters.get("automatic_relevance") == "Relevantes":
            filters.update({"automatic_relevance_class": 1})
        else:
            filters.update({"automatic_relevance_class": 0})
    filters.pop("automatic_relevance", None)

    # Formatação da fonte
    if filters.get("newspaper") == "Todas as fontes":
        filters.pop("newspaper")

    # Formatação da data de início
    if filters.get("begin_date") == "":
        filters.pop("begin_date")
    else:
        date = datetime.combine(filters["begin_date"], datetime.min.time()) # Formata a data para o início do dia
        filters.update({"publication_date": {"$gte": date}})
        filters.pop("begin_date")

    # Formatação da data de fim
    if filters.get("end_date") == "":
        filters.pop("end_date")
    else:
        date = datetime.combine(filters["end_date"], datetime.max.time()) # Formata a data para o fim do dia
        filters["publication_date"].update({"$lte": date})
        filters.pop("end_date")

    # Requisição dos artigoss
    articles_df, search_count = db.get_articles(
        filters,
        as_df=True,
        page=page,
        items_per_page=ITEMS_PER_PAGE,
        sort=INVERSE_FIELDS_MAPPING[sort],
        sort_type={"Ascendente": 1, "Descendente": -1}[sort_type],
    )

    if (articles_df is None) or (not search_count):
        return None, 0

    # Formatação dos valores das células
    articles_df["manual_relevance_class"] = articles_df["manual_relevance_class"].apply(
        lambda x: "Não anotado" if (x is None or np.isnan(x)) else {0: "Irrelevante", 1: "Relevante", 2: "Dúvida"}[x])
        # lambda x: "Não anotado" if (x is None or np.isnan(x)) else ("Relevante" if x == 1 else "Irrelevante"))
    articles_df["automatic_relevance_class"] = articles_df["automatic_relevance_class"].apply(
        lambda x: "Não anotado" if (x is None or np.isnan(x)) else ("Relevante" if x == 1 else "Irrelevante"))
    articles_df["automatic_relevance_pipeline_confidence"] = articles_df["automatic_relevance_pipeline_confidence"].apply(
        lambda x: "" if (x is None or np.isnan(x)) else f"{round(x*100)}%")
    articles_df["publication_date"] = articles_df["publication_date"].apply(
        lambda x: x.strftime("%d/%m/%Y"))

    # Alterando o tipo de id_event para str para melhorar a visualização
    articles_df["id_event"] = articles_df["id_event"].astype(str)
    
    # Mapeamento dos nomes das colunas para o que o usuário deve visualizar
    articles_df.rename(columns=FIELDS_MAPPING, inplace=True)

    # Criação da coluna clicável para abrir a notícia
    articles_df["Abrir"] = articles_df["_id"].apply(
        lambda id: f"?page=article&id={id}"
    )

    # Formatação estética das células
    articles_df = articles_df.style.apply(stylize_relevance_value, subset=FIELDS_MAPPING["manual_relevance_class"]) \
        .apply(stylize_relevance_value, subset=FIELDS_MAPPING["automatic_relevance_class"]) \
            .apply(stylize_confidence_value, subset=FIELDS_MAPPING["automatic_relevance_pipeline_confidence"])

    return articles_df, search_count

def get_sources():
    try:
        return db.get_newspapers()
    except ServerSelectionTimeoutError:
        return None
        
def get_best_classification_model():
    return db.get_best_classification_model()