from configs.domain_list import DomainList

from schemas.util.date import json_date
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
    "start_date": json_date(),
    "end_date": json_date(False),
    "deadline": json_date(),
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
