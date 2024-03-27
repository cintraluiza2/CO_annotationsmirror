from bson.objectid import ObjectId
from typing import Dict, List
# IMPORTS PYMONGO
from pymongo import ASCENDING
from pymongo.errors import DuplicateKeyError

class NewsClassRepository():
    def __init__(self, db_connection) -> None:
        self.__collection_name = "newsData"
        self.__db_connection = db_connection

    # ------------------ Métodos de Inserção ------------------------
    def insert_document_news(self, document: Dict) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.create_index([("title", ASCENDING)], unique=True)
        
        if document['manual_relevance_class'] == '':
            document['manual_relevance_class'] = None
        else:
            document['manual_relevance_class'] = int(document['manual_relevance_class'])
            
        registre = {
            "keyword": document['keyword'],
            "acquisition_date": document['acquisition_date'],
            "publication_date": document['publication_date'],
            "last_update": document['last_update'],
            "newspaper": document['newspaper'],
            "url": document['url'],
            "title": document["title"],
            "article": document['article'],
            "tags": document['tags'],
            "manual_relevance_class": document['manual_relevance_class'],
            "automatic_relevance_class": None,
            "relevance_model": None,
            "relevance_classification_date": None,
            "id_evento": None,
            "resumo": None,
            "data_evento": None,
            "quant_mortes": None,
            "tipo_droga": None,
            "quant_droga": None,
            "pais": None,
            "regiao": None,
            "municipio": None,
            "coordenados GPS": None,
            "tipo_conflito_armado": None,
            "ator1_nome": None,
            "ator1_cod": None,
            "ator2_nome": None,
            "ator2_cod": None,
            "tipo_relacao_entre_atores": None
        }
        try:
            collection.insert_one(registre)
        except DuplicateKeyError:
            return False
        
        return registre

    def insert_list_of_documents_news(self, list_of_documents: List[Dict]) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_many(list_of_documents)
        return list_of_documents

    # ------------------ Métodos de Busca ------------------------
    def select_one_news(self, title, optionsReturn={"_id": 0}) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find_one({"title": title}, optionsReturn)

        return response
    
    def select_many_news(self, filters=None, optionsReturn={"_id": 0}) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(filters, optionsReturn)

        response = []
        for element in data: response.append(element)

        return response

    def select_num_news(self, num: int = 1, filters=None, optionsReturn={"_id": 0}) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(filters, optionsReturn).limit(num)

        response = []
        for element in data: response.append(element)

        return response

    def select_many_order_news(self, filters=None, optionsReturn={"_id": 0, 'accepted_by': 0}, orderFilter=None, optionsFilter=-1) -> List[
        Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(filters, optionsReturn).sort([(orderFilter, optionsFilter)])

        response = []
        for element in data: response.append(element)

        return response

    def select_by_object_id_news(self, objId: ObjectId, optionsReturn=None) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find({"_id": ObjectId(objId)}, optionsReturn)

        response = []
        for element in data: response.append(element)

        return response

    # ------------------ Métodos de Edição ------------------------
    def edit_registry_news(self, title: str, parameterEditing: Dict = None) -> int:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.update_one({"title": title},
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
    
    
