from configs.domain_list import DomainList

from schemas.util.relation import relation

PROJECT_SCHEMA = {
    "title": {
        "type": "string",
        "required": True,
        "unique": True,
        "minlength": 3
    },
    "lead_coordinator": relation(DomainList.PEOPLE, True),
    "coordinators": {
        "type": "list",
        "required": True,
        "schema": relation(DomainList.PEOPLE, True)
    },
    "description": {
        "type": "string",
        "required": True,
        "minlength": 10
    },
    "start_date": {
        "type": "date",
        "required": True
    },
    "end_date": {
        "type": "date"
    },
    "comments": {
        "type": "list",
        "required": True,
        "schema": relation(DomainList.COMMENTS, True),
    },
    "rooms": {
        "type": "list",
        "required": True,
        "schema": relation(DomainList.ROOMS, True),
    },
}
