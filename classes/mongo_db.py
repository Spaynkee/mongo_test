import pymongo

# there's probably a better way to do this.
class Object():
    pass

class mongo_db():
    def __init__(self):
        self.conn = pymongo.MongoClient()
        self.db = self.conn.lol
        self.tables = Object()
        self.get_tables()

    def Store(self, collection, document):
        collection.insert_one(document.__dict__)

    def get_tables(self):
        self.tables.user_data = self.db.loldata
