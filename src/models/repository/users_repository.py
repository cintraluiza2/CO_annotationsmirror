# IMPORTS
from bson.objectid import ObjectId
from typing import Dict, List
# IMPORTS PYMONGO
from pymongo import ASCENDING
from pymongo.errors import DuplicateKeyError
# IMPORTS VALIDATORS
from email_validator import validate_email, EmailNotValidError
import bcrypt
# IMPORTS UTILS
from models.utils.users import Users


class UsersRepository():
    def __init__(self, db_connection) -> None:
        self.__collection_name = "users"
        self.__db_connection = db_connection

    # ------------------ Métodos de Inserção ------------------------
    def insert_user(self, first_name: str, last_name: str, email: str, password: str, role: int) -> bool:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.create_index([("email", ASCENDING)], unique=True)
        try:
            u = Users(first_name, last_name, email, password, role)
            document = u.get_dict()
            collection.insert_one(document)
            
            return True
            
        except DuplicateKeyError as e:
            return False
        
        except EmailNotValidError as e:
            return e
        
    def insert_id_article(self, email, id_article):
        collection = self.__db_connection.get_collection(self.__collection_name)
        user = self.select_one_user(email)
        set_id_article = set(user["id_article"])
        set_id_article.add(id_article)
        num_article = len(set_id_article)
        parameterEditing = {
            "id_article": set_id_article,
            "num_article": num_article
        }
        data = collection.update_one({"email": email},
                                     {"$set": parameterEditing})
        return data.modified_count
        

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
    def edit_registry_user(self, email, first_name, last_name, role) -> int:
        collection = self.__db_connection.get_collection(self.__collection_name)
        parameterEditing = {
            "first_name": first_name,
            "last_name": last_name,
            "role": role,
        }
        data = collection.update_one({"email": email},
                                     {"$set": parameterEditing})
        return data.modified_count
    
    def edit_registry_password(self, email, password) -> int:
        collection = self.__db_connection.get_collection(self.__collection_name)
        password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt(10))
        parameterEditing = {
            "password": password
        }
        data = collection.update_one({"email": email},
                                     {"$set": parameterEditing})
        return data.modified_count

    def delete_registry_user(self, email: str) -> int:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.delete_one({"email": email})

        return data.deleted_count
    
    
