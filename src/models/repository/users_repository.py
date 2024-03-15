# IMPORTS
from bson.objectid import ObjectId
from typing import Dict, List
# IMPORTS PYMONGO
from pymongo import ASCENDING
from pymongo.errors import DuplicateKeyError
# IMPORTS VALIDATORS
from email_validator import validate_email, EmailNotValidError
import bcrypt


class UsersRepository():
    def __init__(self, db_connection) -> None:
        self.__collection_name = "users"
        self.__db_connection = db_connection

    # ------------------ Métodos de Inserção ------------------------
    def insert_user(self, first_name: str, last_name: str, email: str, password: str, role: int, avatar="-") -> bool:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.create_index([("email", ASCENDING)], unique=True)
        try:
            validate_email(email)
            password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt(10))
            document = {
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "password": password,
                "role": role,
                "avatar": avatar,
                "notes": None,
                "num_article_analyzed": 0,
                "num_notes": 0
            }
            collection.insert_one(document)
            
            return True
            
        except DuplicateKeyError as e:
            return False
        
        except EmailNotValidError as e:
            return e

    # ------------------ Métodos de Busca ------------------------
    
    def select_user_pass(self, email: str) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        optionsReturn={"_id": 0}
        document = {
            "email": email
        }
        response = collection.find_one(document, optionsReturn)

        return response

    def select_one_user(self, email: str) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        optionsReturn={"_id": 0, "password": 0}
        document = {
            "email": email
        }
        response = collection.find_one(document, optionsReturn)

        return response

    def select_many_users(self, filters=None) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        optionsReturn = {
            "_id": 0, 
            "last_name": 0, 
            "password": 0,
            "notes": 0,
            "avatar": 0
            }
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
    
    
