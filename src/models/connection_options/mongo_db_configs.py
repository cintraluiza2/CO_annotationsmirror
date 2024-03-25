from dotenv import load_dotenv
import os

load_dotenv(override=True)

user = os.getenv('USERNAME_MONGO')
password = os.getenv('PASSWORD_MONGO')
host = os.getenv('HOST_MONGO')
port = os.getenv('PORT_MONGO')
authentication = os.getenv('AUTHENTICATION_MONGO')
db_name = os.getenv('DB_NAME_MONGO')

mongo_db_infos = {
    "USERNAME": user,
    "PASSWORD": password,
    "HOST": host,
    "PORT": port,
    "AUTHENTICATION": authentication,
    "DB_NAME": db_name
}
