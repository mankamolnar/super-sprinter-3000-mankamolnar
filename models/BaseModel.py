from peewee import *
from models.PsqlHandler import *


class BaseModel(Model):

    class Meta:
        psql_handler = PsqlHandler()
        psql_handler.connect()

        database = psql_handler.get_connection()
