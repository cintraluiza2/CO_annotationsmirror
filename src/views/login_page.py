import streamlit as st

def login_page():
    """Handle the login process."""
    
    st.set_page_config(
        page_title="Login",
        page_icon="📝",
        layout="centered",
    )

    from ..controllers.main_controllers import authenticator # garantindo set_page_config como a primeira execução

    authenticator.login(
        location='main',
        callback=lambda _: st.rerun(),
        fields={
            'Form name':'Entrar no OrgaExtractor',
            'Username':'E-mail ou nome de usuário',
            'Password':'Senha',
            'Login':'Entrar',
            'Captcha':'Captcha'
        }
    )