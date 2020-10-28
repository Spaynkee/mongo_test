class db_adapter():
    def __init__(self, db_class):
        self.schema = db_class
        self.store = db_class.Store
        self.tables = db_class.tables

