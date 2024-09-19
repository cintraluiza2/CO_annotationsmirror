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
    def get_count(self, filters = {}):
        """
        Counts the number of documents in the `newsData` collection that match the given filters.

        Args:
            filters (Dict): Filters to apply to the count query.

        Returns:
            int: Number of documents matching the filters.
        """
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.count_documents(filters)

        return response
    
    def find_all(self):
        """
        Retrieves all documents from the `newsData` collection.

        Returns:
            pymongo.cursor.Cursor: Cursor for iterating over all documents in the collection.
        """
        collection = self.__db_connection.get_collection(self.__collection_name)
        return collection.find()
    
    def select_one_news(self, id_news, optionsReturn={"_id": 0}) -> Dict:
        """
        Retrieves a single news document by its event ID.

        Args:
            id_news: The ID of the news event.
            optionsReturn (Dict): Fields to include or exclude in the returned document.

        Returns:
            Union[Dict, bool]: News document as a dictionary if found, False if not found.
        """
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find_one({"id_event": id_news}, optionsReturn)
        if response == None:
            return False
        n = News(**response)
        n.set_keys()

        return n.get_dict()
    
    def select_note_news(self, id_news, id_user, optionsReturn={"_id": 0}) -> Dict:
        """
        Retrieves a specific note from a news document by event ID and user ID.

        Args:
            id_news: The ID of the news event.
            id_user: The ID of the user who created the note.
            optionsReturn (Dict): Fields to include or exclude in the returned document.

        Returns:
            Union[Dict, bool]: Note as a dictionary if found, False if not found.
        """
        collection = self.__db_connection.get_collection(self.__collection_name)
        news = self.select_one_news(id_news)
        if news:
            notes = news['notes']
            for note in notes:
                if note['id_user'] == id_user:
                    return note
        else:
            return False
         
    def select_many_news(self, filters=None, optionsReturn={"_id": 0}) -> List[Dict]:
        """
        Retrieves multiple news documents that match the given filters.

        Args:
            filters (Dict): Filters to apply to the query.
            optionsReturn (Dict): Fields to include or exclude in the returned documents.

        Returns:
            List[Dict]: List of news documents as dictionaries.
        """
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(filters, optionsReturn)

        response = []
        for element in data: 
            n = News(**element)
            n.set_keys()
            response.append(n.get_dict())

        return response
    

    def select_num_news(self, num: int = 1, filters=None, optionsReturn={"_id": 0}) -> List[Dict]:
        """
        Retrieves a specified number of news documents that match the given filters.

        Args:
            num (int): Number of documents to retrieve.
            filters (Dict): Filters to apply to the query.
            optionsReturn (Dict): Fields to include or exclude in the returned documents.

        Returns:
            List[Dict]: List of news documents as dictionaries.
        """
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
        """
        Retrieves multiple news documents that match the given filters, sorted by a specified field.

        Args:
            filters (Dict): Filters to apply to the query.
            optionsReturn (Dict): Fields to include or exclude in the returned documents.
            orderFilter (str): Field to sort by.
            optionsFilter (int): Sort order; 1 for ascending, -1 for descending.
            model_return (bool): If True, returns documents as `News` objects; otherwise, returns raw documents.

        Returns:
            List[Dict]: List of news documents as dictionaries.
        """
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
        """
        Retrieves news documents by their ObjectId.

        Args:
            objId (ObjectId): The ObjectId of the news document.
            optionsReturn (Dict): Fields to include or exclude in the returned document.

        Returns:
            List[Dict]: List of news documents as dictionaries.
        """
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
        """
        Updates a news document by its event ID with new parameters.

        Args:
            id: The ID of the news event.
            parameterEditing (Dict): Parameters to update.

        Returns:
            int: Number of documents modified.
        """
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.update_one({"id_event": id},
                                     {"$set": parameterEditing})
        return data.modified_count
    
    def edit_registry_note(self, id_news, id_user, parameterEditing: Dict = None):
        """
        Updates a note within a news document by its event ID and user ID.

        Args:
            id_news: The ID of the news event.
            id_user: The ID of the user who created the note.
            parameterEditing (Dict): Parameters to update.

        Returns:
            None
        """
        collection = self.__db_connection.get_collection(self.__collection_name)
        news = self.select_one_news(id_news)
        notes = news['notes']
        t = False
        for note in notes:
            if note['id_user'] == id_user:
                note.update(parameterEditing)
                t = True
                break
        
        if not t:
            parameterEditing["id_user"] = id_user
            notes.append(parameterEditing)
                
        data = collection.update_one({"id_event": id_news}, 
                                    {"$set": {"notes: {notes}"}})

    def edit_many_registries_news(self, filters: Dict = None, parameterEditing: Dict = None) -> int:
        """
        Updates multiple news documents that match the given filters.

        Args:
            filters (Dict): Filters to apply to the update query.
            parameterEditing (Dict): Parameters to update.

        Returns:
            int: Number of documents modified.
        """
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.update_many(filters,
                                      {"$set": parameterEditing})
        return data.modified_count

    def delete_one_registry_news(self, title: str) -> int:
        """
        Deletes a single news document by its title.

        Args:
            title (str): The title of the news document.

        Returns:
            int: Number of documents deleted.
        """
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.delete_one({"title": title})

        return data.deleted_count

    def delete_many_registries_news(self, filters: Dict = None) -> int:
        """
        Deletes multiple news documents that match the given filters.

        Args:
            filters (Dict): Filters to apply to the delete query.

        Returns:
            int: Number of documents deleted.
        """
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.delete_many(filters)

        return data.deleted_count
    
    # ------------------ Métodos de Atualização ------------------------
    def replace_one_registry_news(self, id, registry) -> bool:
        """
        Replaces a news document by its ObjectId with a new document.

        Args:
            id: The ObjectId of the news document.
            registry (Dict): New document data to replace the old one.

        Returns:
            bool: True if the replacement is successful, otherwise an exception.
        """
        try:
            collection = self.__db_connection.get_collection(self.__collection_name)
            print(registry)
            collection.replace_one({"_id": ObjectId(id)}, registry)
            return True
        except Exception as e:
            return e
        
    def update_one_registry_news(self, id, registry):
        """
        Updates a news document by its ObjectId with new data.

        Args:
            id: The ObjectId of the news document.
            registry (Dict): New data to update.

        Returns:
            None
        """
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_one({"_id": ObjectId(id)}, {"$set": registry})
