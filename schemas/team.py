from configs.domain_list import DomainList

from schemas.util.relation import relation

TEAM_SCHEMA = {
    "people": {
        "type": "list",
        "required": True,
        "schema": relation(DomainList.PEOPLE, True)
    },
    "projects": {
        "type": "list",
        "required": True,
        "default": [],
        "schema": relation(DomainList.PROJECTS, True)
    },
    "coordinator": relation(DomainList.PEOPLE, True),
    "comments": {
        "type": "list",
        "required": True,
        "default": [],
        "schema": relation(DomainList.COMMENTS, True)
    },
    "rooms": {
        "type": "list",
        "required": True,
        "default": [],
        "schema": relation(DomainList.ROOMS, True)
    },
}
