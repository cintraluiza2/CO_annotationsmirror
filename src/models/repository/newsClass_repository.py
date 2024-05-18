from bson.objectid import ObjectId
from typing import Dict, List
# IMPORTS UTILS
from models.utils.news import News
# IMPORTS PYMONGO
from pymongo import ASCENDING
from pymongo.errors import DuplicateKeyError

class NewsClassRepository():
    def __init__(self, db_connection) -> None:
        self.__collection_name = "newsData"
        self.__db_connection = db_connection
        self.collection = self.__db_connection.get_collection(self.__collection_name)

    # ------------------ Métodos de Inserção ------------------------
    def insert_document_news(self, document: Dict, model_active=True) -> Dict:
        """
        Insert a document into the newsData collection

        Args:
            document (Dict): Receives the news in dictionary format with the URL as the unique key

        Returns:
            False: Insertion failed
            True: Insertion successful
        """
        collection = self.__db_connection.get_collection(self.__collection_name) # Estabelece conexão com o banco
        collection.create_index("url", unique=True)
        collection.create_index("id_event", unique=True)
        document["id_event"] = self.get_count() 
        if model_active:
            registre.set_keys()
        registre = News(**document)
        try:
            collection.insert_one(registre.get_dict())
        except DuplicateKeyError:
            return False
        
        return True

    def insert_list_of_documents_news(self, documents: List[Dict]) -> List[Dict]:
        """
        Inserts a list of documents into the newsData collection.

        Args:
            document (List[Dict]): Receives a list with news in dictionary format with the URL as the unique key.

        Returns:
            DuplicateKeyError: Duplicate key
            False: Insertion failed.
            True: Insertion successful.
        """
        list_of_documents = []
        for d in documents:
            n = News(**d)
            n.set_keys()
            list_of_documents.append(n.get_dict())
        try:
            collection = self.__db_connection.get_collection(self.__collection_name)
            collection.insert_many(list_of_documents)
        except DuplicateKeyError as e:
            return e
        except:
            return False
        return True

    # ------------------ Métodos de Busca ------------------------
    def get_count(self):
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.count_documents({})

        return response
    
    def find_all(self):
        collection = self.__db_connection.get_collection(self.__collection_name)
        return collection.find()
    
    def select_one_news(self, id_news, optionsReturn={"_id": 0}) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find_one({"id_event": id_news}, optionsReturn)
        if response == None:
            return False
        n = News(**response)
        n.set_keys()

        return n.get_dict()
    
    def select_many_news(self, filters=None, optionsReturn={"_id": 0}) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(filters, optionsReturn)

        response = []
        for element in data: 
            n = News(**element)
            n.set_keys()
            response.append(n.get_dict())

        return response

    def select_num_news(self, num: int = 1, filters=None, optionsReturn={"_id": 0}) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(filters, optionsReturn).limit(num)

        response = []
        for element in data: 
            n = News(**element)
            n.set_keys()
            response.append(n.get_dict())

        return response

    def select_many_order_news(self, filters=None, optionsReturn={"_id": 0}, orderFilter=None, optionsFilter=-1, model_return=True) -> List[
        Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(filters, optionsReturn).sort([(orderFilter, optionsFilter)])

        response = []
        for element in data: 
            if model_return:
                n = News(**element)
                n.set_keys()
                response.append(n.get_dict())
            else:
                response.append(element)

        return response

    def select_by_object_id_news(self, objId: ObjectId, optionsReturn=None) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find({"_id": ObjectId(objId)}, optionsReturn)

        response = []
        for element in data: 
            n = News(**element)
            n.set_keys()
            response.append(n.get_dict())

        return response

    # ------------------ Métodos de Edição ------------------------
    def edit_registry_news(self, id, parameterEditing: Dict = None) -> int:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.update_one({"id_event": id},
                                     {"$set": parameterEditing})
        return data.modified_count

    def edit_many_registries_news(self, filters: Dict = None, parameterEditing: Dict = None) -> int:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.update_many(filters,
                                      {"$set": parameterEditing})
        return data.modified_count

    def delete_one_registry_news(self, title: str) -> int:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.delete_one({"title": title})

        return data.deleted_count

    def delete_many_registries_news(self, filters: Dict = None) -> int:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.delete_many(filters)

        return data.deleted_count
    
    # ------------------ Métodos de Atualização ------------------------
    def replace_one_registry_news(self, id, registry) -> bool:
        try:
            collection = self.__db_connection.get_collection(self.__collection_name)
            print(registry)
            collection.replace_one({"_id": ObjectId(id)}, registry)
            return True
        except Exception as e:
            return e
        
    def update_one_registry_news(self, id, registry):
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_one({"_id": ObjectId(id)}, {"$set": registry})
