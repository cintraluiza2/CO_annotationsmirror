import streamlit as st
import atexit

from src.controllers.home_controllers import is_admin
from src.views import login_page, home_page, article_page, register_page
from src.data.database import close_ssh_tunnel

# Para fechar o túnel SSH quando a aplicação é encerrada
atexit.register(close_ssh_tunnel)

def main():
    params = st.query_params

    if "page" in params and params["page"] == "article":
        article_page()
    elif "page" in params and params["page"] == "register":
        if is_admin(st.session_state["username"]):
            register_page()
        else:
            home_page()
    else:
        home_page()

def app():
    if not st.session_state.get("authentication_status"):
        login_page()
        if st.session_state.get("authentication_status") == False:
            st.error("Usuário ou senha incorretos.")

    if st.session_state.get("authentication_status"):
        main()

if __name__ == "__main__":
    app()
