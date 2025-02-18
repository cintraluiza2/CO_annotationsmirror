from pymongo.errors import ServerSelectionTimeoutError
import streamlit as st
import atexit

from src.views import login_page, home_page, article_page
from src.data.database import close_ssh_tunnel

atexit.register(close_ssh_tunnel)

# Initialize session state variables if they don't exist
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'username' not in st.session_state:
    st.session_state.username = ''

def main():
    params = st.query_params
    if "page" in params and params["page"] == "article":
        article_page()
    else:
        home_page()

def app():
    # if not st.session_state.authenticated:
    #     login_page()
    # else:
    #     main()
    main()

if __name__ == "__main__":
    app()
