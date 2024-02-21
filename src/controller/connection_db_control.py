# IMPORTS BASICS
import sys
from typing import List
# IMPORTS DATA
from models.connection_options.connection import DBConnectionHandler
from models.repository.newsClass_repository import NewsClassRepository

class ConnectionsDBControl():
    def __init__(self) -> None:
        self.__db_handle = DBConnectionHandler()
        self.__db_handle.connect_to_db()
        self.__db_connection = self.__db_handle.get_db_connection()
        self.__repository = NewsClassRepository(self.__db_connection)
