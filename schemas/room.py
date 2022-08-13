from configs.domain_list import DomainList

from schemas.util.relation import relation

ROOM_SCHEMA = {
    "title": {
        "type": "string",
        "required": True,
        "minlength": 3,
    },
    "admins": {
        "type": "list",
        "required": True,
        "minlength": 1,
        "schema": relation(DomainList.PEOPLE),
    },
    "people": {
        "type": "list",
        "required": True,
        "minlength": 2,
        "schema": relation(DomainList.PEOPLE),
    },
}
