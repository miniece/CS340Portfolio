# Example Python Code to Insert a Document 
from pymongo import MongoClient
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password):
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
        self.client = MongoClient('mongodb://%s:%s@%s:%d/?authSource=admin' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        """Insert a document into the animals collection.
           Returns True if the insert succeeded, False otherwise."""
        if data is not None:
            try:
                result = self.database.animals.insert_one(data)  # data should be dictionary
                return result.acknowledged
            except Exception as e:
                print("Insert failed: %s" % e)
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Create method to implement the R in CRUD.
    def read(self, criteria=None):
        """Query documents from the animals collection.
           Returns a list of matching documents, or an empty list."""
        try:
            if criteria is not None:
                cursor = self.database.animals.find(criteria, {"_id": False})
            else:
                cursor = self.database.animals.find({}, {"_id": False})
            return list(cursor)  # convert the cursor to a list
        except Exception as e:
            print("Query failed: %s" % e)
            return []

    # Create method to implement the U in CRUD.
    def update(self, criteria, change):
        """Update documents in the animals collection.
           criteria: dictionary of key/value pairs to match
           change:   dictionary of key/value pairs to set
           Returns the number of documents modified."""
        if criteria is not None and change is not None:
            try:
                result = self.database.animals.update_many(criteria, {"$set": change})
                return result.modified_count
            except Exception as e:
                print("Update failed: %s" % e)
                return 0
        else:
            raise Exception("Nothing to update, because criteria or change parameter is empty")
            

    # Create method to implement the D in CRUD.
    def delete(self, criteria):
        """Remove documents from the animals collection.
           criteria: dictionary of key/value pairs to match
           Returns the number of documents removed."""
        if criteria is not None:
            try:
                result = self.database.animals.delete_many(criteria)
                return result.deleted_count
            except Exception as e:
                print("Delete failed: %s" % e)
                return 0
        else:
            raise Exception("Nothing to delete, because criteria parameter is empty")