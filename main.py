""" main.py

This is the main.py file for my database adapter test program. I made this to make sure
I could do this before switching my actual project over to use one of these,
if I still intend to do so.

The goal was to make a generic adapter for any kind of database to be able to be used by
my project, so long as we could create a custom class for storing, updating, deleting,
and reading data.

I currently have that implemented for (inserting and selecting) with both mongo and sql.

"""

from classes.sql_db import SqlDb
from classes.mongo_db import MongoDb
from classes.db_adapter import DbAdapter
from models.user_data import UserData

def main():
    """
        The main function creates a db_adapter, instantiates it with a specific class
        (currently either sql or mongo), and then uses one of our data models
        to store and retrieve data to the db pointed to from the adapter.
    """

    db_adapt = DbAdapter(SqlDb())
    #db_adapt = DbAdapter(MongoDb())

    data_object = UserData()
    data_object.match_id = "12"
    data_object.player = "player"

    db_adapt.store(db_adapt.tables.user_data, data_object)
    results = db_adapt.get_table(db_adapt.tables.user_data)
    print(results)

if __name__ == "__main__":
    main()
