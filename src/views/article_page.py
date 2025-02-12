from datetime import datetime
import streamlit as st
import pandas as pd

from ..controllers.article_controllers import get_article

keys = iter(range(1, 100))

st.session_state["tab_name"] = "| Notícia"



def display_article_form(key, disabled=True, submit_label="Salvar", **kwargs):
    with st.form(key, enter_to_submit=False):
        st.header("Dados preenchidos automaticamente")

        relevance = st.radio("Relevante?", ["Sim", "Não"], horizontal=True, index=kwargs.get('relevance'), key=next(keys), disabled=disabled)

        if kwargs.get("confidence"):
            confidence = kwargs.get("confidence")*100
            if confidence >= 90:
                st.markdown(f"Confiança: :rainbow[{(confidence):.0f}%]")
            elif confidence <= 75:
                st.markdown(f"Confiança: :red[{(confidence):.0f}%]")
            else:
                st.markdown(f"Confiança: {(confidence):.0f}%")

        country = st.selectbox("País", options=["Brasil", "Argentina", "..."], index=kwargs.get('country'), key=next(keys), disabled=disabled)    
        region = st.text_input("Região", value=kwargs.get('region'), disabled=disabled)
        city = st.text_input("Município", value=kwargs.get('city'), disabled=disabled)

        date = st.date_input("Data do evento", format="DD/MM/YYYY", value=datetime.strptime(kwargs.get('date'), "%d/%m/%Y"), disabled=disabled)

        location = st.text_input("Latitude e longitude", placeholder="Ex: 18.25000000, -63.16666666", value=kwargs.get('location'), disabled=disabled)
        # st.map()

        col1, col2 = st.columns(2, gap="small")
        with col1:
            conflict = st.radio("Houve conflito?", ["Sim", "Não"], index=kwargs.get('conflict'), disabled=disabled, key=next(keys))
        with col2:
            deaths = st.number_input("Quantidade de mortes", min_value=0, value=kwargs.get('deaths'), disabled=disabled)
        
        # Drogas apreendidas
        df = pd.DataFrame(columns=["Tipo de droga", "Quantidade", "Métrica"], data=kwargs.get('drugs'))
        st.data_editor(
            df,
            column_config={
                "Tipo de droga": st.column_config.SelectboxColumn(options=["Cocaína", "Skunk"], required=True, disabled=disabled),
                "Quantidade": st.column_config.NumberColumn(format="%f", required=True, disabled=disabled),
                "Métrica": st.column_config.SelectboxColumn(options=["gramas", "quilos", "tabletes"], required=True, disabled=disabled)
            },
            hide_index=True,
            use_container_width=True,
            num_rows="dynamic",
            disabled=disabled,
        )

        # Armas apreendidas
        df = pd.DataFrame(columns=["Tipo de arma", "Quantidade"])
        st.data_editor(
            df,
            column_config={
                "Tipo de arma": st.column_config.TextColumn(required=True, disabled=disabled),
                "Quantidade": st.column_config.NumberColumn(required=True, format="%d", disabled=disabled)
            },
            hide_index=True,
            use_container_width=True,
            num_rows="dynamic",
            disabled=disabled,
        )

        # Relação entre atores
        df = pd.DataFrame(columns=["Ator 1", "Ator 2", "Relação"])
        st.data_editor(
            df,
            column_config={
                "Ator 1": st.column_config.TextColumn(required=True, disabled=disabled),
                "Ator 2": st.column_config.TextColumn(required=True, disabled=disabled),
                "Relação": st.column_config.SelectboxColumn(required=True, options=["Rivalidade", "Competição"], disabled=disabled)
            },
            hide_index=True,
            use_container_width=True,
            num_rows="dynamic",
            disabled=disabled,
        )

        st.form_submit_button(submit_label)

params = st.query_params

def display_article(container):
    article = get_article(_id=st.query_params.get("id"))

    st.header("Dados da notícia")
    st.text(f"Aquisição: {article.get('acquisition_date')}")
    st.text(f"Publicação: {article.get('publication_date')}")
    st.text(f"Última atualização: {article.get('last_update')}")
    st.text(f"Fonte: {article.get('newspaper')}")
    st.text_area(label="Título da notícia", value=article.get("title"), height=68)
    st.text_area(label="Corpo da notícia:", value=article.get("article"), height=680)
    st.link_button("Acessar página da notícia", url=article.get("url"))

def article_page():
    st.set_page_config(
        page_title="| Notícia",
        page_icon="📝",
        layout="wide",
    )
    # st.title("Anotação de notícia")

    col1, col2 = st.columns(2, gap="medium")

    with col1:
        display_article(col1)

    with col2:
        with st.form("human_annotation", enter_to_submit=False):
            st.header("Anotação humana")

            relevance = st.radio("Relevante?", ["Sim", "Não"], horizontal=True)
            doubt = st.checkbox(label="Com dúvida")

            country = st.selectbox("País", options=["Brasil", "Argentina", "..."])
            region = st.text_input("Região")
            city = st.text_input("Município")

            date = st.date_input("Data do evento", format="DD/MM/YYYY")

            location = st.text_input("Latitude e longitude", placeholder="Ex: 18.25000000, -63.16666666")
            # st.map()

            col2_1, col2_2 = st.columns(2, gap="small")
            with col2_1:
                conflict = st.radio("Houve conflito?", ["Sim", "Não"], help="Conflito é caracterizado como...", index=None, key=next(keys))
            with col2_2:
                deaths = st.number_input("Quantidade de mortes", value=0, min_value=0)
            
            # Drogas apreendidas
            df = pd.DataFrame(columns=["Tipo de droga", "Quantidade", "Métrica"])
            st.data_editor(
                df,
                column_config={
                    "Tipo de droga": st.column_config.SelectboxColumn(options=["Cocaína", "Skunk"], required=True),
                    "Quantidade": st.column_config.NumberColumn(format="%f", required=True),
                    "Métrica": st.column_config.SelectboxColumn(options=["gramas", "quilos", "tabletes"], required=True)
                },
                hide_index=True,
                use_container_width=True,
                num_rows="dynamic",
            )

            # Armas apreendidas
            df = pd.DataFrame(columns=["Tipo de arma", "Quantidade"])
            st.data_editor(
                df,
                column_config={
                    "Tipo de arma": st.column_config.TextColumn(required=True),
                    "Quantidade": st.column_config.NumberColumn(required=True, format="%d")
                },
                hide_index=True,
                use_container_width=True,
                num_rows="dynamic",
            )

            # Relação entre atores
            df = pd.DataFrame(columns=["Ator 1", "Ator 2", "Relação"])
            st.data_editor(
                df,
                column_config={
                    "Ator 1": st.column_config.TextColumn(required=True),
                    "Ator 2": st.column_config.TextColumn(required=True),
                    "Relação": st.column_config.SelectboxColumn(required=True, options=["Rivalidade", "Competição"])
                },
                hide_index=True,
                use_container_width=True,
                num_rows="dynamic",
            )

            st.form_submit_button("Salvar")

    st.divider()

    display_article_form(key="automatic_annotation", submit_label="Usar dados", **{
        'relevance': not 1,
        'confidence': 0.97967,
        'country': 1,
        'region': "Nordeste",
        "city": None,
        "date": "12/03/2025",
        "drugs": [
            {"Tipo de droga": "Cocaína", "Quantidade": 500, "Métrica": "gramas"}
        ]
    })

    article_id = params.get("id", [None])[0]
    print(f"article_id: {article_id}")
