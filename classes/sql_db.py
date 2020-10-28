import configparser
import sqlalchemy as db # type: ignore

# there's probably a better way to do this.
class Object():
    pass

class sql_db():

    def __init__(self):

        self._config = configparser.ConfigParser()
        self._config.read('general.cfg')

        self.db_host = self._config.get('DATABASE', 'db_id')
        self.db_user = self._config.get('DATABASE', 'db_user')
        self.db_pw = self._config.get('DATABASE', 'db_password')
        self.db_name = self._config.get('DATABASE', 'db_name')

        self.engine = db.create_engine('mysql+pymysql://{}:{}@{}/{}?charset=utf8'.format(\
                self.db_user, self.db_pw, self.db_host, self.db_name), pool_size=100, max_overflow=100)
        self.connection = self.engine.connect()
        self.metadata = db.MetaData()

        self.champs_table = db.Table('champions', self.metadata, autoload=True,\
                autoload_with=self.engine)
        # change this to sqlalchemy?
        self.tables = Object()
        self.get_tables()


    def Store(self, table, row_object):
        table_insert = table.insert().values(row_object.__dict__)
        self.connection.execute(table_insert)

    def get_tables(self):
        self.tables.user_data = test_table = db.Table('test', self.metadata, autoload=True, autoload_with=self.engine)
