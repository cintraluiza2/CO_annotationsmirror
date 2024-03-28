from dotenv import load_dotenv
import os

load_dotenv(override=True)

user = "couser"
password = os.getenv('PASSWORD_MONGO')
host = "localhost"
port = "27018"
authentication = "couser"
db_name = "couser"

mongo_db_infos = {
    "USERNAME": user,
    "PASSWORD": password,
    "HOST": host,
    "PORT": port,
    "AUTHENTICATION": authentication,
    "DB_NAME": db_name
}
