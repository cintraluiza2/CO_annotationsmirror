from datetime import datetime
from math import ceil
import streamlit as st

from ..controllers.home_controllers import get_articles_dataframe, get_sources, get_best_classification_model
from src.settings import (
    ITEMS_PER_PAGE, COLUMNS_ORDER, APP_NAME, APP_DESCRIPTION, APP_INSTRUCTIONS, APP_ICON
)

keys = iter(range(1, 100))

if "filters" not in st.session_state:
    st.session_state["filters"] = {}

def display_welcome():
    st.title(APP_NAME)
    st.text(APP_DESCRIPTION)
    st.text(APP_INSTRUCTIONS)

    display_problem_reporting()

def display_problem_reporting():
    global keys
    try:
        st.button("Reportar problema", disabled=True, key=next(keys))
    except StopIteration:
        keys = iter(range(1, 100))
        st.button("Reportar problema", disabled=True, key=next(keys))

def display_automatic_annotation_button():
    columns = st.columns(3)
    best_classification_model = get_best_classification_model()
    score = best_classification_model.get("score", "Desconhecida")
    last_evaluation = best_classification_model.get('timestamp', "Desconhecido")

    columns[0].markdown(f"Acurácia do modelo de classificação automática: **{round(score*100)}%**")
    columns[1].write(f"Última avaliação: {last_evaluation}")
    global keys
    try:
        columns[2].button("Atualizar anotação automática", disabled=True, key=next(keys))
    except StopIteration:
        keys = iter(range(1, 100))
        columns[2].button("Atualizar anotação automática", disabled=True, key=next(keys))

def display_search_count(count):
    st.write(f"{count} notícias encontradas")

def display_pagination(total_pages):
    st.write(f"Página {st.session_state.current_page} de {total_pages}")

    pagination = st.columns(2, gap="large")
    if st.session_state.current_page > 1:
        pagination[0].button("← Página anterior", on_click=previous_page, use_container_width=True)

    if st.session_state.current_page < total_pages:
        global keys
        try:
            pagination[1].button("Próxima página →", on_click=next_page, use_container_width=True, key=next(keys))
        except StopIteration:
            keys = iter(range(1, 100))
            pagination[1].button("Próxima página →", on_click=next_page, use_container_width=True, key=next(keys))

def display_articles_dataframe(df):
    """
    Exibe o dataframe de notícias.
    """
    st.dataframe(
        df,
        hide_index=True,
        column_order=COLUMNS_ORDER,
        column_config={
            "_id": None,
            "Abrir": st.column_config.LinkColumn(label="", display_text="Abrir", pinned=True),
            "Validada": st.column_config.CheckboxColumn(label="Validada")
        },
        key="dataframe_widget",
        height=600,
        use_container_width=True
    )

def search():
    st.session_state.df, st.session_state.search_count = get_articles_dataframe(
        filters=st.session_state.filters,
        page=st.session_state.current_page,
        sort=st.session_state.get("sort_input"),
        sort_type=st.session_state.get('sort_type_input')
    )
    df = st.session_state.df
    if st.session_state.search_count > 0:
        display_automatic_annotation_button()
        display_search_count(st.session_state.search_count)
        display_articles_dataframe(df)
        display_pagination(total_pages=ceil(st.session_state.search_count/ITEMS_PER_PAGE))
        display_problem_reporting()
    else:
        st.info("Nenhum resultado encontrado para os filtros selecionados.")

def next_page():
    apply_filters_form(mode="next_page")

def previous_page():
    apply_filters_form(mode="previous_page")

def apply_filters_form(mode): # "next_page", "previous_page" ou "search"
    if mode == "search":
        st.session_state.current_page = 1
    elif mode == "next_page":
        st.session_state.current_page += 1
    elif mode == "previous_page":
        st.session_state.current_page -= 1

    st.session_state.filters = {
        'title': st.session_state.get("title_input", ""),
        'begin_date': st.session_state.get("begin_date_input", ""),
        'end_date': st.session_state.get("end_date_input", ""),
        'manual_relevance': st.session_state.get("manual_relevance_input", None),
        'automatic_relevance': st.session_state.get("automatic_relevance_input", None),
        'newspaper': st.session_state.get("newspaper_input", None)
    }

    with st.spinner("Por favor, aguarde...", show_time=True):
        search()

def create_sidebar(messages_placeholder):
    st.sidebar.title("Filtros")

    with st.sidebar.form("filters_form", enter_to_submit=True):
        st.text_input("Título da notícia:", key="title_input")

        # Filtros de data
        col1, col2 = st.columns(2)
        begin_date = col1.date_input(
            "De:",
            min_value=datetime(2011, 1, 1),
            max_value=datetime.today(),
            value=datetime(2011, 1, 1),
            format="DD/MM/YYYY",
            disabled=False,
            key="begin_date_input"
        )
        end_date = col2.date_input(
            "Até:",
            min_value=datetime(2011, 1, 1),
            max_value=datetime.today(),
            value=datetime.today(),
            format="DD/MM/YYYY",
            disabled=False,
            key="end_date_input"
        )

        # Filtro de relevância manual
        st.selectbox(
            "Anotação manual:",
            options=["Todas", "Relevantes", "Irrelevantes", "Dúvida", "Sem anotação"],
            on_change=None,
            key="manual_relevance_input",
        )

        # Filtro de relevância automática
        st.selectbox(
            "Anotação automática:",
            options=["Todas", "Relevantes", "Irrelevantes"],
            on_change=None,
            key="automatic_relevance_input",
        )

        # Filtro de fonte
        newspapers = get_sources()
        if newspapers is None:
            messages_placeholder.error((
                "Desculpe, parece que não estamos conseguindo nos conectar com o banco de dados agora 😕\n\n"
                "Por favor, tente em um outro momento..."
            ))
            newspapers = []
        st.selectbox(
            "Fonte:",
            options=["Todas as fontes"] + newspapers,
            key="newspaper_input",
            placeholder="Escolha uma fonte de notícias"
        )

        # Ordenação
        st.selectbox(
            "Ordenar por:",
            options=["Confiança", "Data de publicação", "Fonte", "ID", "Título da notícia"],
            key="sort_input",
        )

        st.selectbox(
            "Tipo de ordenação:",
            options=["Ascendente", "Descendente"],
            key="sort_type_input"
        )
        
        # Aplicação do filtro
        st.form_submit_button("Buscar", on_click=lambda: apply_filters_form(mode="search"))

def home_page():
    st.set_page_config(
        page_title=APP_NAME,
        page_icon=APP_ICON,
        layout="wide",
        initial_sidebar_state="expanded"
    )

    if 'current_page' not in st.session_state:
        st.session_state.current_page = 1

    messages_placeholder = st.empty()

    create_sidebar(messages_placeholder)

    if "df" in st.session_state:
        # search()
        pass
    else:
        display_welcome()
