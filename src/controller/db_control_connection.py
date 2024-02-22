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
        
    def check_password(self, userName: str, password: str) -> Tuple:
        cpf = CPF()
        # VALIDATE CPF
        if cpf.validate(userName) or userName == "123.123.123-12":
            # TREATMENT OF INPUTS
            userName = userName.replace(".", "").replace("-", "")
            
            # USER SEARCH
            user = self.__users_repository.select_one({'userName': userName})
            
            # CHECK USER AND PASSWORD
            if user and user['password'] == password:
                return (True, user['userType'])
            else:
                return (False, "USER") # Invalid username or password
        else:
            return (False, "CPF") # Invalid  CPF
