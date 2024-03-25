# Imports Basics
import pandas as pd
import numpy as np
# Imports Data
from models.connection_options.connection import DBConnectionHandler
from models.repository.newsClass_repository import NewsClassRepository

class DataFrame:
    def __init__(self) -> None:
        # DB_VARIABLES
        # Create a new instance of DBConnectionHandler
        self.__db_handle = DBConnectionHandler()
        # Connect to the database using the DBConnectionHandler instance
        self.__db_handle.connect_to_db()
        self.__db_connection = self.__db_handle.get_db_connection()
        self.__news_repository = NewsClassRepository(self.__db_connection)
        
        self.make_data_frame()
        
    def make_data_frame(self):
        news = self.__news_repository.select_many_news()
        dataframe = pd.DataFrame(news)

        return dataframe
