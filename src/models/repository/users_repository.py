# IMPORTS
from bson.objectid import ObjectId
from typing import Dict, List
# IMPORTS PYMONGO
from pymongo import ASCENDING
from pymongo.errors import DuplicateKeyError
# IMPORTS VALIDATORS
from email_validator import validate_email, EmailNotValidError


class UsersRepository():
    def __init__(self, db_connection) -> None:
        self.__collection_name = "users"
        self.__db_connection = db_connection

    # ------------------ Métodos de Inserção ------------------------
    def insert_user(self, name: str, email: str, password: str, role: int, avatar="-") -> bool:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.create_index([("email", ASCENDING)], unique=True)
        try:
            validate_email(email)
            document = {
                "name": name,
                "email": email,
                "password": password,
                "role": role,
                "avatar": avatar
            }
            collection.insert_one(document)
            
        except DuplicateKeyError as e:
            return e
        
        except EmailNotValidError as e:
            return e

    # ------------------ Métodos de Busca ------------------------

    def select_one_user(self, email: str, password: str) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        optionsReturn={"_id": 0, "password": 0}
        document = {
            "email": email,
            "password": password
        }
        response = collection.find_one(document, optionsReturn)

        return response

    def select_many_users(self, filters=None) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        optionsReturn={"_id": 0, "password": 0}
        data = collection.find(filters, optionsReturn)

        response = []
        for element in data: response.append(element)

        return response

    # ------------------ Métodos de Edição ------------------------
    def edit_registry_user(self, email: str, parameterEditing: Dict = None) -> int:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.update_one({"email": email},
                                     {"$set": parameterEditing})
        return data.modified_count

    def delete_registry_user(self, email: str) -> int:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.delete_one({"email": email})

        return data.deleted_count
    
    
