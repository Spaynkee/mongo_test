from classes.mongo_db import mongo_db
from classes.sql_db import sql_db
from classes.db_adapter import db_adapter
from models.userDataModel import userDataModel


# right, so, this script will create a new DB object, and pass in some kind of identifier.
# we will then call store, update, get, and delete, to make sure they work.
def main():

    #db = db_adapter(mongo_db())
    db = db_adapter(sql_db())

    data_object = userDataModel()
    data_object.match_id = "ok"
    data_object.player = "player"
    db.store(db.tables.user_data, data_object)


if __name__ == "__main__":
    main()
