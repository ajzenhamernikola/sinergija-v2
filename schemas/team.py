from configs.domain_list import DomainList

from schemas.util.relation import relation

TEAM_SCHEMA = {
    "coordinator": relation(DomainList.PEOPLE),
    "people": {
        "type": "list",
        "required": True,
        "minlength": 1,
        "schema": relation(DomainList.PEOPLE)
    },
    "projects": {
        "type": "list",
        "required": True,
        "default": [],
        "schema": relation(DomainList.PROJECTS)
    },
    "comments": {
        "type": "list",
        "required": True,
        "default": [],
        "schema": relation(DomainList.COMMENTS)
    },
    "rooms": {
        "type": "list",
        "required": True,
        "default": [],
        "schema": relation(DomainList.ROOMS)
    },
}
