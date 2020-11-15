""" mongo_db.py class

This class holds all of the properties and objects used by the adapter to handle db transactions.
This class will allow the adapter to work with mongo dbs, using pymongo

"""
import pymongo
from models.tables import Tables

def deco(cls):
    """ decorator needed to set the tables property

        I honestly don't remember why this was needed.
    """
    cls.tables = cls.get_tables()
    return cls

@deco
class MongoDb():
    """
        Contains all the needed properties and functions for the adapter to hook in to.

        Attributes:
            conn    (obj): pymongo connection object
            mdb     (obj): mongo database object
            tables  (Tables): object used to store references to db collections
    """

    conn = pymongo.MongoClient()
    mdb = conn.lol

    @classmethod
    def store(cls, collection, document):
        """ allows pymongo to use our db_adapter to store data

            Args:
                collection: the collection we're storing data into.
                document: an object populated with the data we're storing.

        """
        collection.insert_one(document.__dict__)

    @classmethod
    def get_table(cls, collection):
        """ allows pymongo to use our db_adapter to get all documents in a collection

            Args:
                collection: the collection we're getting data from

        """
        return list(collection.find())

    @classmethod
    def get_one(cls, collection, document):
        """ allows pymongo to use our db_adapter to get a single document

            Args:
                collection: the collection we're getting data from
                document: an object populated with the data we're getting.

        """
        return collection.find_one(vars(document))

    @classmethod
    def delete(cls, collection, document):
        """ allows the adapter to use pymongo to delete data

            Args:
                collection: the collection we're deleting data from
                document: the object we're deleting

        """

    @classmethod
    def update(cls, collection, document):
        """ allows the adapter to use pymongo to update data

            Args:
                collection: the collection we're udpating data from
                document: the object we're updating

        """


    @classmethod
    def get_tables(cls):
        """ sets our tables object for this database class

            Returns:
                our_tables: an object with references to mongo db collections
        """
        our_tables = Tables()
        our_tables.user_data = cls.mdb.loldata

        return our_tables
