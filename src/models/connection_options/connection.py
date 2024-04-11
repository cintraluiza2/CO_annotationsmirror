from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
import yaml

class DBConnectionHandler():
    def __init__(self) -> None:
        with open('mongo_configs.yml', 'r', encoding='utf-8') as file:
            mongo_db_infos = yaml.safe_load(file)
        
        self.__connection_string = 'mongodb://{}:{}@{}:{}/{}?directConnection=true&serverSelectionTimeoutMS=2000'.format(
            mongo_db_infos["username"],
            mongo_db_infos["password"],
            mongo_db_infos["host"],
            mongo_db_infos["port"],
            mongo_db_infos["authentication"]
        )
        # self.__connection_string = "mongodb://localhost:27017/"
        self.__database_name = mongo_db_infos["DB_NAME"]
        self.__client = None
        self.__db_connection = None

    def connect_to_db(self):
        self.__client = MongoClient(self.__connection_string)
        try:
            self.__client.server_info()
            self.__db_connection = self.__client[self.__database_name]
            return True
        except ServerSelectionTimeoutError:
            return False

    def get_db_connection(self):
        return self.__db_connection

    def get_db_client(self):
        return self.__client
