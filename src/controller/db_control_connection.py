# IMPORTS BASICS
from validate_docbr import CPF
from typing import Tuple
# IMPORTS DATA
from models.connection_options.connection import DBConnectionHandler
from models.repository.newsClass_repository import NewsClassRepository
from models.repository.users_repository import UsersRepository

class DBControlConnections():
    def __init__(self) -> None:
        self.__db_handle = DBConnectionHandler()
        self.__db_handle.connect_to_db()
        self.__db_connection = self.__db_handle.get_db_connection()
        self.__news_repository = NewsClassRepository(self.__db_connection)
        self.__users_repository = UsersRepository(self.__db_connection)
        
    def users_check_password(self, userName: str, password: str) -> Tuple:
        # TREATMENT OF INPUTS
        userName = userName.replace(".", "").replace("-", "")
            
        # USER SEARCH
        user = self.__users_repository.select_one({'userName': userName})
            
        # CHECK USER AND PASSWORD
        if user and user['password'] == password:
            return (True, user['userType'])
        else:
            return (False, None) # Invalid username or password
        
    def news_list_table(self):
        # DATA NEWS
        list_news = self.__news_repository.select_many(optionsReturn={"_id": 0, "keyword": 0, "acquisition_date":0, "last_update": 0, "url": 0, "tags": 0, "article": 0, "manual_relevance_class": 0, "relevance_classification_date": 0, "relevance_model": 0})
        return list_news
