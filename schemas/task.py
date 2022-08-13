from configs.domain_list import DomainList

from schemas.util.relation import relation

TASK_SCHEMA = {
    "person": relation(DomainList.PEOPLE),
    "assignees": {
        "type": "list",
        "required": True,
        "minlength": 1,
        "schema": relation(DomainList.PEOPLE)
    },
    "team": relation(DomainList.TEAMS, False),
    "project": relation(DomainList.PROJECTS, False),
    "title": {
        "type": "string",
        "required": True,
        "minlength": 10,
        "maxlength": 100
    },
    "description": {
        "type": "string",
        "required": True,
        "minlength": 10,
    },
    "start_date": {
        "type": "date",
        "required": True
    },
    "end_date": {
        "type": "date"
    },
    "deadline": {
        "type": "date",
        "required": True
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
