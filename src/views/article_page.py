from datetime import datetime
import streamlit as st
import pandas as pd

from ..controllers.article_controllers import get_article, regex_search, update_article_on_db, get_countries, domain_translation
from ..settings import ACTORS_RELATIONS, DEFAULT_DRUGS_METRICS, DEFAULT_DRUGS, BRAZILIAN_STATES

# keys = iter(range(1, 100))

st.session_state["tab_name"] = "| Notícia"

# def display_article_form(key, disabled=True, submit_label="Salvar", **kwargs):
#     with st.form(key, enter_to_submit=False):
#         st.header("Dados preenchidos automaticamente")

#         relevance = st.radio("Relevante?", ["Sim", "Não"], horizontal=True, index=kwargs.get('relevance'), key=next(keys), disabled=disabled)

#         if kwargs.get("confidence"):
#             confidence = kwargs.get("confidence")*100
#             if confidence >= 90:
#                 st.markdown(f"Confiança: :rainbow[{(confidence):.0f}%]")
#             elif confidence <= 75:
#                 st.markdown(f"Confiança: :red[{(confidence):.0f}%]")
#             else:
#                 st.markdown(f"Confiança: {(confidence):.0f}%")

#         country = st.selectbox("País", options=LATIN_AMERICA_CONTRIES, index=kwargs.get('country'), key=next(keys), disabled=disabled)    
#         region = st.text_input("Região", value=kwargs.get('region'), disabled=disabled)
#         city = st.text_input("Município", value=kwargs.get('city'), disabled=disabled)

#         date = st.date_input("Data do evento", format="DD/MM/YYYY", value=datetime.strptime(kwargs.get('date'), "%d/%m/%Y"), disabled=disabled)

#         location = st.text_input("Latitude e longitude", placeholder="Ex: 18.25000000, -63.16666666", value=kwargs.get('location'), disabled=disabled)
#         # st.map()

#         col1, col2 = st.columns(2, gap="small")
#         with col1:
#             conflict = st.radio("Houve conflito?", ["Sim", "Não"], index=kwargs.get('conflict'), disabled=disabled, key=next(keys))
#         with col2:
#             deaths = st.number_input("Quantidade de mortes", min_value=0, value=kwargs.get('deaths'), disabled=disabled)
        
#         # Drogas apreendidas
#         df = pd.DataFrame(columns=["Tipo de droga", "Quantidade", "Métrica"], data=kwargs.get('drugs'))
#         st.data_editor(
#             df,
#             column_config={
#                 "Tipo de droga": st.column_config.SelectboxColumn(options=["Cocaína", "Skunk"], required=True, disabled=disabled),
#                 "Quantidade": st.column_config.NumberColumn(format="%f", required=True, disabled=disabled),
#                 "Métrica": st.column_config.SelectboxColumn(options=["gramas", "quilos", "tabletes"], required=True, disabled=disabled)
#             },
#             hide_index=True,
#             use_container_width=True,
#             num_rows="dynamic",
#             disabled=disabled,
#         )

#         # Armas apreendidas
#         df = pd.DataFrame(columns=["Tipo de arma", "Quantidade"])
#         st.data_editor(
#             df,
#             column_config={
#                 "Tipo de arma": st.column_config.TextColumn(required=True, disabled=disabled),
#                 "Quantidade": st.column_config.NumberColumn(required=True, format="%d", disabled=disabled)
#             },
#             hide_index=True,
#             use_container_width=True,
#             num_rows="dynamic",
#             disabled=disabled,
#         )

#         # Relação entre atores
#         df = pd.DataFrame(columns=["Ator 1", "Ator 2", "Relação"])
#         st.data_editor(
#             df,
#             column_config={
#                 "Ator 1": st.column_config.TextColumn(required=True, disabled=disabled),
#                 "Ator 2": st.column_config.TextColumn(required=True, disabled=disabled),
#                 "Relação": st.column_config.SelectboxColumn(required=True, options=["Rivalidade", "Competição"], disabled=disabled)
#             },
#             hide_index=True,
#             use_container_width=True,
#             num_rows="dynamic",
#             disabled=disabled,
#         )

#         st.form_submit_button(submit_label)

params = st.query_params

def display_article(article):
    # article = get_article(_id=st.query_params.get("id"))
    article_body = article.get("article")

    # Avaliação automática e confiança
    col_auto1, col_auto2 = st.columns(2, gap="small")
    
    # Avaliação automática
    automatic_class = article.get("automatic_relevance_class")
    if automatic_class is not None:
        relevance_text = {0: "Não relevante", 1: "Relevante"}.get(automatic_class, "Não classificado")
        relevance_color = {0: "red", 1: "green"}.get(automatic_class, "gray")
        col_auto1.markdown(f"**Avaliação automática**: :{relevance_color}[{relevance_text}]")
    else:
        col_auto1.markdown("**Avaliação automática**: Não classificado")
    
    # Confiança
    confidence = article.get("automatic_relevance_pipeline_confidence")
    if confidence is not None:
        confidence_percent = confidence * 100
        if confidence_percent >= 90:
            col_auto2.markdown(f"**Confiança**: :blue[{confidence_percent:.1f}%]")
        elif confidence_percent <= 75:
            col_auto2.markdown(f"**Confiança**: :red[{confidence_percent:.1f}%]")
        else:
            col_auto2.markdown(f"**Confiança**: :orange[{confidence_percent:.1f}%]")
    else:
        col_auto2.markdown("**Confiança**: -")

    col1, col2 = st.columns(2, gap="small")
    # Palavras-chave
    if article.get("accepted_by"):
        regex_terms = article.get("accepted_by")
        regex_terms = regex_terms.split(" - ") if isinstance(regex_terms, str) else regex_terms
        keywords = regex_search(article_body, regex_terms)
        col1.pills("Palavras-chave:", keywords, disabled=False)

    # Tags
    if tags:=article.get("tags"):
        col2.pills("Tags:", tags, disabled=False)

    # Datas
    col1, col2 = st.columns(2, gap="small")
    col1.markdown(f"**Publicação**: {article.get('publication_date')}")
    last_update = article.get('last_update')
    col2.markdown(f"**Última atualização**: {last_update if last_update else "-"}")

    col1, col2 = st.columns(2, gap="small")
    col1.markdown(f"**Fonte**: {article.get('newspaper')}")
    col2.markdown(f"**ID**: {article.get("id_event")}")
    
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

    # CSS para remover scroll principal e estilizar containers
    st.markdown("""
        <style>
        /* Remove apenas o scroll vertical da página principal */
        section.main {
            overflow-y: hidden !important;
            overflow-x: auto !important;
        }
        
        .block-container {
            padding-top: 1rem !important;
            padding-bottom: 1rem !important;
        }
        
        /* Garante que elementos dentro do container sejam visíveis */
        [data-testid="stVerticalBlock"] {
            display: block !important;
        }
        
        [data-testid="stVerticalBlock"] > div > div {
            display: block !important;
        }
        
        /* Scrollbar customizada para os containers internos */
        div[data-testid="stVerticalBlock"]::-webkit-scrollbar {
            width: 8px;
        }
        
        div[data-testid="stVerticalBlock"]::-webkit-scrollbar-track {
            background: #f0f0f0;
            border-radius: 4px;
        }
        
        div[data-testid="stVerticalBlock"]::-webkit-scrollbar-thumb {
            background: #888;
            border-radius: 4px;
        }
        
        div[data-testid="stVerticalBlock"]::-webkit-scrollbar-thumb:hover {
            background: #555;
        }
        </style>
    """, unsafe_allow_html=True)

    article_id = params.get("id", [None])
    article = get_article(_id=article_id)

    # Adiciona espaço acima das colunas
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Usa altura dinâmica baseada no viewport
    container_height = 850  # Altura em pixels (aumentada)
    
    col1, col2 = st.columns(2, gap="small")

    with col1:
        with st.container(height=container_height, border=False):
            display_article(article)

    with col2:
        with st.container(height=container_height, border=False):
            with st.form("human_annotation", enter_to_submit=False):
                st.header("Anotação humana")

                # Relevância
                st.radio(
                    "Relevante?",
                    ["Não", "Sim", "Dúvida"],
                    horizontal=True,
                    key="manual_relevance_input",
                    index=article.get("manual_relevance_class", None)
                )

                # Validação da anotação
                st.radio(
                    "Esta anotação foi validada pelo(a) professor(a) responsável?",
                    ["Não", "Sim"],
                    horizontal=True,
                    key="validated_input",
                    index=article.get("validated", 0)
                )

                # País
                countries = [c["description"] for c in get_countries()] # Obtendo todos os países conhecidos no banco
                # Obtendo o índice do país salvo no banco, se houver:
                index = countries.index(domain_translation("country", value=article["country"])) if article.get("country") else None
                st.selectbox(
                    "País:",
                    options=countries,
                    index=index,
                    placeholder="Selecione o país",
                    key="country_input",
                )

                # Estado
                state_index = BRAZILIAN_STATES.index(article.get("state")) if article.get("state") in BRAZILIAN_STATES else None
                st.selectbox(
                    "Estado:",
                    options=BRAZILIAN_STATES,
                    index=state_index,
                    placeholder="Selecione o estado",
                    key="state_input"
                )

                # Cidade
                st.text_input("Município:", value=article.get("city"), key="city_input")

                # Referências do local
                st.text_input("Referências do local (se houver):", value=article.get("location_references"), key="location_references_input")

                # Latitude e Longitude
                st.text_input(
                    "Latitude e longitude",
                    value=article.get("latitude_and_longitude"),
                    placeholder="Ex: 18.25000000, -63.16666666",
                    key="latitude_and_longitude_input"
                )

                # Data do evento
                st.date_input(
                    "Data do evento",
                    format="DD/MM/YYYY",
                    value=article.get("event_date"),
                    key="event_date_input"
                )

                # Conflito
                col2_1, col2_2 = st.columns(2, gap="small")
                with col2_1:
                    st.radio(
                        "Houve conflito?",
                        ["Não", "Sim"],
                        help="Conflito é caracterizado como...",
                        index=article.get("conflict"),
                        key="conflict_input"
                    )
                # Mortes
                with col2_2:
                    st.number_input(
                        "Quantidade de mortes",
                        value=article.get("deaths", 0), min_value=0, key="deaths_input")

                st.divider()
                
                # Drogas apreendidas
                st.write("Identifique abaixo as drogas apreendidas, se houver:")
                drugs_df = article["drugs"]
                drugs_input = st.data_editor(
                    drugs_df,
                    column_config={
                        "Tipo de droga": st.column_config.SelectboxColumn(options=DEFAULT_DRUGS, required=True, default=" "),
                        "Quantidade": st.column_config.NumberColumn(format="%f", required=True, default=0),
                        "Métrica": st.column_config.SelectboxColumn(options=DEFAULT_DRUGS_METRICS, required=True, default=" ")
                    },
                    hide_index=True,
                    use_container_width=True,
                    num_rows="dynamic",
                    key="drugs_df_input",
                )

                st.write("Utilize o campo abaixo se desejar adicionar outros tipos de drogas ou outros tipos de métrica:")
                other_drugs_df = article["other_drugs"]
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
                guns_df = article["guns"]
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
                # actors_df = pd.DataFrame(columns=["Ator 1", "Ator 2", "Relação"])
                actors_df = article["actors"]
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

                    same_event_df = article["same_event_articles_id"]
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
                    try:
                        with st.spinner("Por favor, aguarde...", show_time=True):
                            status, message = update_article_on_db(
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
                                    "validated": st.session_state.get("validated_input", None),
                                }
                            )
                    except Exception as e:
                        print(e)
                        st.error("Ocorreu algum erro ao tentar salvar!")
                    else:
                        if status == 0:
                            st.error(message)
                        else:
                            st.success("Salvo com sucesso!")

    # display_article_form(key="automatic_annotation", submit_label="Usar dados", **{
    #     'relevance': not 1,
    #     'confidence': 0.97967,
    #     'country': 1,
    #     'region': "Nordeste",
    #     "city": None,
    #     "date": "12/03/2025",
    #     "drugs": [
    #         {"Tipo de droga": "Cocaína", "Quantidade": 500, "Métrica": "gramas"}
    #     ]
    # }) # Sem suporte ainda
