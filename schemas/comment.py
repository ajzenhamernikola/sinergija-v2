from configs.domain_list import DomainList

from schemas.util.relation import relation

COMMENT_SCHEMA = {
    "person": relation(DomainList.PEOPLE, True),
    "text": {
        "type": "string",
        "required": True,
        "minlength": 2
    }
}
