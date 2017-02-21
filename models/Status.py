from models.BaseModel import *


class Status(BaseModel):
    name = CharField()

    @classmethod
    def get_all_status(cls):
        all_status = cls.select()
        statuses = []
        for status in all_status:
            statuses.append({"id": status.id, "name": status.name})

        return statuses
