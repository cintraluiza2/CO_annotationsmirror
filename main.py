import streamlit as st
import atexit

from src.views import home_page, article_page
from src.data.database import close_ssh_tunnel

# Para fechar o túnel SSH quando a aplicação é encerrada
atexit.register(close_ssh_tunnel)

def app():
    params = st.query_params

    if "page" in params and params["page"] == "article":
        article_page()
    else:
        home_page()

if __name__ == "__main__":
    app()
