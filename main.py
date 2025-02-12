from pymongo.errors import ServerSelectionTimeoutError
import streamlit as st

from src.views import login_page, home_page, article_page
from src.data.database import close_ssh_tunnel

def main():
    params = st.query_params
    if "page" in params and params["page"] == "article":
        article_page()
    else:
        home_page()

def app():
    # if not st.session_state.authenticated:
    #     login()
    # else:
    #     main()
    main()

if __name__ == "__main__":
    try:
        app()
    except Exception as e:
        close_ssh_tunnel()
        raise e
