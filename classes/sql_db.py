""" SqlDb.py class

This class holds all of the properties and objects used by the adapter to handle db transactions.
This class will allow the adapter to work with sql databases, using sqlalchemy.

"""
import configparser
import sqlalchemy as db # type: ignore
from models.tables import Tables

def deco(cls):
    """ decorator needed to set the tables property

        I honestly don't remember why this was needed.
    """
    cls.tables = cls.get_tables()
    return cls

@deco
class SqlDb():
    """
        Contains all the needed properties and functions for the adapter to hook in to.

        Attributes:

            _config         (obj): ConfigParser object for reading config file

            db_host        (str): database host address from config file
            db_user        (str): database user from config file
            db_pw          (str): database user password from config file
            db_name        (str): database name from config file

            engine        (obj): Sqlalchemy engine object created with config file contents
            connection    (obj): Sqlalchemy connection object created from the sqla engine
            metadata      (obj): Database metadata object

            tables        (Tables): object used to store references to db tables

    """

    _config = configparser.ConfigParser()
    _config.read('general.cfg')

    db_host = _config.get('DATABASE', 'db_id')
    db_user = _config.get('DATABASE', 'db_user')
    db_pw = _config.get('DATABASE', 'db_password')
    db_name = _config.get('DATABASE', 'db_name')

    engine = db.create_engine('mysql+pymysql://{}:{}@{}/{}?charset=utf8'.format(\
    db_user, db_pw, db_host, db_name), pool_size=100, max_overflow=100)

    connection = engine.connect()
    metadata = db.MetaData()

    @classmethod
    def store(cls, table, row_object):
        """ allows the adapter to use this type of db to store data.

            Args:
                table: the table object we're storing data into.
                row_object: an object populated with the data we're storing.

        """
        table_insert = table.insert().values(vars(row_object))
        cls.connection.execute(table_insert)


    @classmethod
    def get_table(cls, table):
        """ allows the adapter to use this type of db to get data.

            Args:
                table: the table object we're getting data from.
                row_object: an object populated with the data we're getting.

            Returns:
                All results from the query

        """
        table_select = db.select([table])
        return cls.connection.execute(table_select).fetchall()

    @classmethod
    def get_one(cls, table, row_object):
        """ allows the adapter to use this type of db to get data.

            Args:
                table: the table object we're getting data from.
                row_object: an object populated with the data we're getting.

            Returns:
                All results from the query

        """
        return "not yet implemented"

    @classmethod
    def update(cls, table, row_object):
        """ allows the adapter to use this type of db to update data.

            Args:
                table: the table object we're updating data in.
                row_object: an object populated with the data we're updating.

        """

    @classmethod
    def delete(cls, table, row_object):
        """ allows the adapter to use this type of db to delete data.

            Args:
                table: the table object we're deleting data from.
                row_object: an object populated with the data we're deleting.

        """

    @classmethod
    def get_tables(cls):
        """ sets the tables object for this database class

            Returns:
                our_tables: an object with references to slqa table objects

        """
        our_tables = Tables()
        our_tables.user_data = db.Table('test', cls.metadata,\
                autoload=True, autoload_with=cls.engine)

        return our_tables
