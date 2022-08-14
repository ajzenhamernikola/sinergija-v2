from configs.domain_list import DomainList
from db.base_mongo_operations import BaseMongoDomainOperations


class PeopleMongoOperations(BaseMongoDomainOperations):
    def __init__(self) -> None:
        super().__init__(DomainList.PEOPLE)

    def find_one_by_username(self, username: str):
        return self.collection.find_one({"username": username})
