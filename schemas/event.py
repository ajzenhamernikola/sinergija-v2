from configs.domain_list import DomainList

from schemas.util.date import json_date
from schemas.util.relation import relation
from schemas.util.time import TIME_SCHEMA

EVENT_SCHEMA = {
    "project": relation(DomainList.PROJECTS),
    "title": {
        "type": "string",
        "required": True,
        "minlength": 10,
        "maxlength": 100
    },
    "start_date": json_date(),
    "end_date": json_date(),
    "start_time": {
        "type": "dict",
        "schema": TIME_SCHEMA
    },
    "end_time": {
        "type": "dict",
        "schema": TIME_SCHEMA
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
    }
}
