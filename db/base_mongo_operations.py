from bson.objectid import ObjectId
from configs.domain_list import DomainList
from eve import ID_FIELD
from flask import current_app as app


class BaseMongoDomainOperations:
    def __init__(self, domain: DomainList) -> None:
        self.collection = self.get_mongo_collection(domain)

    def get_mongo_collection(domain: DomainList):
        return app.data.driver.db[domain]

    def find_by_id(self, id: str) -> None:
        return self.collection.find_one({ID_FIELD, ObjectId(id)})
