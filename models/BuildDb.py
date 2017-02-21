from models.UserStories import *
from models.Status import *


class BuildDb:

    def __init__(self, db):
        self.db = db
        self.db_tables = [
            UserStories,
            Status
        ]

    def start(self):
        if self.tables_exist() is False:
            self.build()

    def build(self):
        self.db.drop_tables(self.db_tables, safe=True)
        self.db.create_tables(self.db_tables, safe=True)

        self.create_statuses()

    def tables_exist(self):
        for table in self.db_tables:
            if table.table_exists() is False:
                return False
        return True

    def create_statuses(self):
        Status.create(name='Planning')
        Status.create(name='To do')
        Status.create(name='In progress')
        Status.create(name='Review')
        Status.create(name='Done')
