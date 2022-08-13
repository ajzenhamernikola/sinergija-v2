COMMENT_SCHEMA = {
    "person": {
        "type": "objectid",
        "required": True,
        "data_relation": {
            "resource": "people",
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
