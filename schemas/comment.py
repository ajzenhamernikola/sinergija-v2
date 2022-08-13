from configs.domain_list import DomainList

COMMENT_SCHEMA = {
    "person": {
        "type": "objectid",
        "required": True,
        "data_relation": {
            "resource": DomainList.PEOPLE,
            "field": "_id",
            "embeddable": True
        }
    },
    "text": {
        "type": "string",
        "required": True,
        "minlength": 2
    }
}
