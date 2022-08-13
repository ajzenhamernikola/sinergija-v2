from configs.domain_list import DomainList

from schemas.util.relation import relation

COMMENT_SCHEMA = {
    "person": relation(DomainList.PEOPLE),
    "text": {
        "type": "string",
        "required": True,
        "minlength": 2
    }
}
