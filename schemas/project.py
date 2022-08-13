from configs.domain_list import DomainList

from schemas.util.relation import relation

PROJECT_SCHEMA = {
    "title": {
        "type": "string",
        "required": True,
        "unique": True,
        "minlength": 3
    },
    "lead_coordinator": relation(DomainList.PEOPLE),
    "coordinators": {
        "type": "list",
        "required": True,
        "default": [],
        "schema": relation(DomainList.PEOPLE)
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
        "default": [],
        "schema": relation(DomainList.COMMENTS),
    },
    "rooms": {
        "type": "list",
        "required": True,
        "default": [],
        "schema": relation(DomainList.ROOMS),
    },
}
