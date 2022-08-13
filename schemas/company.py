from configs.domain_list import DomainList

from schemas.util.relation import relation

COMPANY_SCHEMA = {
    "title": {
        "type": "string",
        "required": True,
        "minlength": 2,
    },
    "tags": {
        "type": "list",
        "schema": {
            "type": "string",
            "required": True,
            "minlength": 2,
        },
    },
    "contacts": {
        "type": "list",
        "required": True,
        "default": [],
        "schema": relation(DomainList.CONTACTS),
    },
    "website": {
        "type": "string",
        "regex": "^https?:\/\/.+\..+$",
    },
    "address": {
        "type": "string",
        "minlength": 2,
    },
    "logo": {
        "type": "media",
    }
}
