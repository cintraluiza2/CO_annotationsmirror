from streamlit_authenticator import Authenticate

from src.data.database import get_users_credentials

users_credentials = get_users_credentials()

authenticator = Authenticate(
    credentials=users_credentials,
    cookie_name="co-annotador-cookie",
    cookie_key="5&jivkD%AW@AQGv",
    cookie_expiry_days=0,
    auto_hash=False
)