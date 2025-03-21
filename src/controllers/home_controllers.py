from pymongo.errors import ServerSelectionTimeoutError
import numpy as np

from ..settings import (
    CONFIDENCE_SCALE, DEFAULT_SORTING_FIELD, ITEMS_PER_PAGE, FIELDS_MAPPING, INVERSE_FIELDS_MAPPING
)
from ..data.database import get_articles, get_newspapers, get_best_classification_model

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
        else:
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

    articles_df, search_count = get_articles(
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
        lambda x: "Não anotado" if (x is None or np.isnan(x)) else ("Relevante" if x == 1 else "Irrelevante"))
    articles_df["automatic_relevance_class"] = articles_df["automatic_relevance_class"].apply(
        lambda x: "Não anotado" if (x is None or np.isnan(x)) else ("Relevante" if x == 1 else "Irrelevante"))
    articles_df["automatic_relevance_pipeline_confidence"] = articles_df["automatic_relevance_pipeline_confidence"].apply(
        lambda x: "" if (x is None or np.isnan(x)) else f"{round(x*100)}%")

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
        return get_newspapers()
    except ServerSelectionTimeoutError:
        return None
        