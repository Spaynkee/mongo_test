""" DbAdapter Class

    This class accepts a database class, and sets properties from that class, so that
    theoretically, any database that I set up a class for will work with our db transactions.

"""
class DbAdapter(): # pylint: disable=too-few-public-methods
    """ This class translates our passed db_class methods and properties to ones that can be used
        from our program no matter the db system that is being used.

        Properties:
            schema:      (obj) the type of db we're using
            store:       (obj) the store function we're using
            get_table:   (obj) the get_table function we're using
            get_one:     (obj) the get_one function we're using
            update:      (obj) the update function we're using
            delete:      (obj) the delete function we're using
            tables:      (obj) the tables object we're storing our tables into

    """

    def __init__(self, db_class):
        self.schema = db_class
        self.store = db_class.store
        self.get_table = db_class.get_table
        self.get_one = db_class.get_one
        self.update = db_class.update
        self.delete = db_class.delete
        self.tables = db_class.tables
