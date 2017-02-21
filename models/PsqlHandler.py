from peewee import *
import db_config


class PsqlHandler:

    def __init__(self):
        self.db = False

    def connect(self):
        self.db = PostgresqlDatabase(db_config.psql_db, user=db_config.psql_user, password=db_config.psql_pass)

    def get_connection(self):
        return self.db
