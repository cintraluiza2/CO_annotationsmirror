from datetime import datetime
import streamlit as st
import pandas as pd

from ..controllers.article_controllers import get_article, regex_search, update_article_on_db
from ..settings import ACTORS_RELATIONS, LATIN_AMERICA_CONTRIES

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

        country = st.selectbox("País", options=LATIN_AMERICA_CONTRIES, index=kwargs.get('country'), key=next(keys), disabled=disabled)    
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
    article_body = article.get("article")

    col1, col2 = st.columns(2, gap="small")
    # Palavras-chave
    if article.get("accepted_by"):
        regex_terms = article.get("accepted_by")
        regex_terms = regex_terms.split(" - ") if isinstance(regex_terms, str) else regex_terms
        keywords = regex_search(article_body, regex_terms)
        col1.pills("Palavras-chave:", keywords, disabled=True)

    # Tags
    if tags:=article.get("tags"):
        col2.pills("Tags:", tags, disabled=True)

    st.text(f"Publicação: {article.get('publication_date')}")
    st.text(f"Última atualização: {article.get('last_update')}")
    st.text(f"Fonte: {article.get('newspaper')}")
    st.text_area(label="Título da notícia", value=article.get("title"), height=68)
    st.text_area(label="Corpo da notícia:", value=article_body, height=680)
    
    if url:=article.get("url"):
        if isinstance(url, str):
            st.link_button("Acessar página da notícia", url=url)

def article_page():
    st.set_page_config(
        page_title="| Notícia",
        page_icon="📝",
        layout="wide",
    )

    col1, col2 = st.columns(2, gap="medium")

    with col1:
        display_article(col1)

    with col2:
        with st.form("human_annotation", enter_to_submit=False):
            st.header("Anotação humana")

            # Relevância
            st.radio("Relevante?", ["Sim", "Não", "Dúvida"], horizontal=True, key="manual_relevance_input")

            # Localização
            st.selectbox("País:", options=LATIN_AMERICA_CONTRIES, index=None, placeholder="Selecione o país", key="country_input")
            st.text_input("Estado:", key="state_input")
            st.text_input("Município:", key="city_input")
            st.text_input("Referências do local (se houver):", key="location_references_input")
            st.text_input("Latitude e longitude", placeholder="Ex: 18.25000000, -63.16666666", key="latitude_and_longitude_input")

            # Data do evento
            st.date_input("Data do evento", format="DD/MM/YYYY", value=None, key="event_date_input")

            # Conflito
            col2_1, col2_2 = st.columns(2, gap="small")
            with col2_1:
                st.radio("Houve conflito?", ["Sim", "Não"], help="Conflito é caracterizado como...", index=None, key="conflict_input")
            with col2_2:
                st.number_input("Quantidade de mortes", value=0, min_value=0, key="deaths_input")

            st.divider()
            
            # Drogas apreendidas
            st.write("Identifique abaixo as drogas apreendidas, se houver:")
            drugs_df = pd.DataFrame(columns=["Tipo de droga", "Quantidade", "Métrica"])
            drugs_input = st.data_editor(
                drugs_df,
                column_config={
                    "Tipo de droga": st.column_config.SelectboxColumn(options=["Cocaína", "Skunk"], required=True, default=" "),
                    "Quantidade": st.column_config.NumberColumn(format="%f", required=True, default=0),
                    "Métrica": st.column_config.SelectboxColumn(options=["gramas", "quilos", "tabletes"], required=True, default=" ")
                },
                hide_index=True,
                use_container_width=True,
                num_rows="dynamic",
                key="drugs_df_input",
            )

            st.write("Utilize o campo abaixo se desejar adicionar outros tipos de drogas ou outros tipos de métrica:")
            other_drugs_df = pd.DataFrame(columns=["Outro tipo de droga", "Quantidade", "Métrica"])
            other_drugs_input = st.data_editor(
                other_drugs_df,
                column_config={
                    "Outro tipo de droga": st.column_config.TextColumn(required=False, default=" "),
                    "Quantidade": st.column_config.NumberColumn(format="%f", required=True, default=0),
                    "Métrica": st.column_config.TextColumn(required=True, default=" ")
                },
                hide_index=True,
                use_container_width=True,
                num_rows="dynamic",
                key="other_drugs_df_input",
            )

            st.divider()

            # Armas apreendidas
            st.write("Identifique abaixo as armas apreendidas, se houver:")
            guns_df = pd.DataFrame(columns=["Tipo de arma", "Quantidade"])
            guns_input = st.data_editor(
                guns_df,
                column_config={
                    "Tipo de arma": st.column_config.TextColumn(required=True, default=" "),
                    "Quantidade": st.column_config.NumberColumn(required=True, format="%d", default=0)
                },
                hide_index=True,
                use_container_width=True,
                num_rows="dynamic",
            )

            st.divider()

            # Relação entre atores
            st.write("Identifique abaixo a interações entre os atores envolvidos:")
            actors_df = pd.DataFrame(columns=["Ator 1", "Ator 2", "Relação"])
            actors_input = st.data_editor(
                actors_df,
                column_config={
                    "Ator 1": st.column_config.TextColumn(required=True, default=" "),
                    "Ator 2": st.column_config.TextColumn(required=True, default=" "),
                    "Relação": st.column_config.SelectboxColumn(required=True, options=ACTORS_RELATIONS, default=" ")
                },
                hide_index=True,
                use_container_width=True,
                num_rows="dynamic",
            )

            st.divider()

            col2_1, col2_2 = st.columns(2, gap="small")
            with col2_1:
                # Outras notícias sobre o mesmo evento
                st.write("Identifique abaixo o ID de outras notícias que tratam sobre este mesmo evento, se houver:")
                same_event_df = pd.DataFrame(columns=["ID da notícia"])
                same_event_input = st.data_editor(
                    same_event_df,
                    column_config={
                        "ID da notícia": st.column_config.NumberColumn(required=True, format="%d")
                    },
                    hide_index=True,
                    use_container_width=True,
                    num_rows="dynamic",
                )

            if st.form_submit_button("Salvar"):

                update_article_on_db(
                    _id=st.query_params.get("id"),
                    update={
                        "manual_relevance_class": st.session_state.get("manual_relevance_input", None),
                        "country": st.session_state.get("country_input", None),
                        "state": st.session_state.get("state_input", None),
                        "city": st.session_state.get("city_input", None),
                        "location_references": st.session_state.get("location_references_input", None),
                        "latitude_and_longitude": st.session_state.get("latitude_and_longitude_input", None),
                        "event_date": st.session_state.get("event_date_input", None),
                        "conflict": st.session_state.get("conflict_input", None),
                        "deaths": st.session_state.get("deaths_input", None),
                        "drugs": drugs_input,
                        "other_drugs": other_drugs_input,
                        "guns": guns_input,
                        "actors": actors_input,
                        "same_event": same_event_input,
                    }
                )

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

    article_id = params.get("id", [None])
    print(get_article(_id=article_id))