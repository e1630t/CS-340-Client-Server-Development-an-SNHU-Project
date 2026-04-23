# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 
from typing import Dict, Any, List, Optional   # Added for type hints

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username: str, password: str):
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = username 
        PASS = password
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient(f'mongodb://{USER}:{PASS}@{HOST}:{PORT}')
        self.database = self.client[DB]
        self.collection = self.database[COL]

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data: Dict[str, Any]) -> bool:
        """
        Insert a new document into the animals collection.

        :param data: Dictionary representing the document to insert.
        :return: True if successful insert, else False.
        """
        #2.aReturn “True” if successful insert, else “False”
        if data is not None and isinstance(data, dict): 
            try:
                result = self.collection.insert_one(data)  # data should be dictionary
                return True if result.inserted_id else False
            except Exception as e:
                print("Create Error:", e)
                return False
        else: 
            return False

    # Create method to implement the R in CRUD.
    def read(self, query: Dict[str, Any], projection: Optional[Dict[str, int]] = None) -> List[Dict[str, Any]]:
        """
        Retrieve documents from the animals collection.

        :param query: MongoDB filter dictionary.
        :param projection: Optional projection dictionary to limit returned fields.
        :return: List of documents matching the query.
        """
        #2.b Return result in a list if the command is successful, else an empty list.
        if query is not None and isinstance(query, dict):
            try:
                return list(self.collection.find(query, projection))
            except Exception as e:
                print("Read Error:", e)
                return []
        else:
             return []

    # Use the update function to query for and change document(s) for the U of CRUD
    def update(self, query: Dict[str, Any], new_values: Dict[str, Any]) -> int:
        """
        Update documents in the animals collection.

        :param query: Filter dictionary to match documents.
        :param new_values: Dictionary of fields to update.
        :return: Number of modified documents.
        """
        if query is None or new_values is None:
            raise Exception("Error: Value is not present to make changes to.")
        try:
            result = self.collection.update_many(query, {"$set": new_values})
            return result.modified_count
        except Exception as e:
            print("Error:", e)
            return 0

    # Use the delete function for D in CRUD to remove document(s)
    def delete(self, query: Dict[str, Any]) -> int:
        """
        Delete documents from the animals collection.

        :param query: Filter dictionary to match documents.
        :return: Number of deleted documents.
        """
        if query is None:
            raise Exception("Error: Value is not present to delete.")
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count  # return number of documents deleted
        except Exception as e:
            print("Error:", e)
            return 0
