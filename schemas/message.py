from configs.domain_list import DomainList

from schemas.util.relation import relation

MESSAGE_SCHEMA = {
    "room": relation(DomainList.ROOMS),
    "sender": relation(DomainList.PEOPLE),
    "readers": {
        "type": "list",
        "required": True,
        "default": [],
        "schema": relation(DomainList.PEOPLE),
    },
    "text": {
        "type": "string",
        "required": True,
    },
    "sending_datetime": {
        "type": "datetime",
        "required": True,
    }
}
