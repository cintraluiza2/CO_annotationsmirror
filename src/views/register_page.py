import streamlit as st

from ..controllers.register_controllers import user_exists, is_valid_email, register_user

def register_page():
    st.set_page_config(
        page_title="Cadastro de usuário",
        page_icon="📝",
        layout="centered",
    )

    if st.button("Voltar ao início"):
        if "page" in st.query_params:
            del st.query_params["page"]
        st.rerun()

    st.title("Cadastro")

    email = st.text_input("E-mail do novo usuário")
    role = st.selectbox("Nível de acesso", options=["Administrador", "Anotador"])

    if st.button("Cadastrar"):
        if not email:
            st.error("Preencha todos os campos.")
        elif user_exists(email):
            st.error("Usuário já existe.")
        elif not is_valid_email(email): # Adicionar verificação de que a string é um e-mail
            st.error("Insira um e-mail válido")
        else:
            password = register_user(email, role)
            if password:
                st.success(
                    "Usuário cadastrado com sucesso!\n\n"
                    "Copie as credenciais de acesso, elas não aparecerão novamente:\n\n"
                    f"E-mail: {email}\n\n"
                    f"Senha: {password}"
                )
            else:
                st.error("Erro ao cadastrar usuário")
    