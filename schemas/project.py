from configs.domain_list import DomainList

PROJECT_SCHEMA = {
    "title": {
        "type": "string",
        "required": True,
        "unique": True,
        "minlength": 3
    },
    "lead_coordinator": {
        "type": "objectid",
        "required": True,
        "data_relation": {
            "resource": DomainList.PEOPLE,
            "field": "_id",
            "embeddable": True
        }
    },
    "coordinators": {
        "type": "list",
        "required": True,
        "schema": {
            "type": "objectid",
            "data_relation": {
                "resource": DomainList.PEOPLE,
                "field": "_id",
                "embeddable": True
            }
        },
    },
    "description": {
        "type": "string",
        "required": True,
        "minlength": 10
    },
    "start_date": {
        "type": "date",
        "required": True
    },
    "end_date": {
        "type": "date"
    },
    "comments": {
        "type": "list",
        "required": True,
        "schema": {
            "type": "objectid",
            "data_relation": {
                "resource": DomainList.COMMENTS,
                "field": "_id",
                "embeddable": True
            }
        },
    },
    "rooms": {
        "type": "list",
        "required": True,
        "schema": {
            "type": "objectid",
            "data_relation": {
                "resource": DomainList.ROOMS,
                "field": "_id",
                "embeddable": True
            }
        },
    },
}
