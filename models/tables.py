""" tables.py class

    This class should have a property for every table, defined as None when its instantiated,
    but then able to be set afterward by any db class that we create. so we know where to store
    or read data from.

"""
class Tables(): # pylint: disable=too-few-public-methods
    """ The tables class holds all the tables we have in our database schema
        It will be overwritten by individual database classes as needed.

    """

    def __init__(self):
        # all our 'tables' will be added here.
        self.user_data = None
