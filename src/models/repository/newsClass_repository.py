from bson.objectid import ObjectId
from typing import Dict, List


class NewsClassRepository():
    def __init__(self, db_connection) -> None:
        self.__collection_name = "newsClass"
        self.__db_connection = db_connection

    # ------------------ Métodos de Inserção ------------------------
    def insert_document(self, document: Dict) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(document)
        return document

    def insert_list_of_documents(self, list_of_documents: List[Dict]) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_many(list_of_documents)
        return list_of_documents

    # ------------------ Métodos de Busca ------------------------
    def select_many(self, filters=None, optionsReturn={"_id": 0}) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(filters, optionsReturn)

        response = []
        for element in data: response.append(element)

        return response

    def select_one(self, filters=None, optionsReturn={"_id": 0}) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find_one(filters, optionsReturn)

        return response

    def select_num(self, num: int = 1, filters=None, optionsReturn={"_id": 0}) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(filters, optionsReturn).limit(num)

        response = []
        for element in data: response.append(element)

        return response

    def select_if_property_exists(self, property, optionsReturn={"_id": 0}) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find({property: {"$exists": True}}, optionsReturn)

        response = []
        for element in data: response.append(element)

        return response

    def select_many_order(self, filters=None, optionsReturn={"_id": 0}, orderFilter=None, optionsFilter=-1) -> List[
        Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(filters, optionsReturn).sort([(orderFilter, optionsFilter)])

        response = []
        for element in data: response.append(element)

        return response

    def select_or_propertys(self, property: List[Dict] = None, optionsReturn={"_id": 0}) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find({"$or": property}, optionsReturn)

        response = []
        for element in data: response.append(element)

        return response

    def select_by_object_id(self, objId: ObjectId, optionsReturn=None) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find({"_id": ObjectId(objId)}, optionsReturn)

        response = []
        for element in data: response.append(element)

        return response

    # ------------------ Métodos de Edição ------------------------
    def edit_registry(self, objId: ObjectId = None, parameterEditing: Dict = None) -> int:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.update_one({"_id": ObjectId(objId)},
                                     {"$set": parameterEditing})
        return data.modified_count

    def edit_many_registries(self, filters: Dict = None, parameterEditing: Dict = None) -> int:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.update_many(filters,
                                      {"$set": parameterEditing})
        return data.modified_count

    def edit_many_increment(self, filters: Dict = None, parameterEditing: Dict = None) -> int:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.update_many(filters,
                                      {"$inc": parameterEditing})
        return data.modified_count

    def delete_one_registry(self, filters: Dict = None) -> int:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.delete_one(filters)

        return data.deleted_count

    def delete_many_registries(self, filters: Dict = None) -> int:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.delete_many(filters)

        return data.deleted_count
