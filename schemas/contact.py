CONTACT_SCHEMA = {
    "first_name": {
        "type": "string",
        "required": True,
        "minlength": 2,
        "maxlength": 50,
    },
    "last_name": {
        "type": "string",
        "required": True,
        "minlength": 2,
        "maxlength": 50,
    },
    "mobile": {
        "type": "string",
        "minlength": 9,
        "maxlength": 10,
        "regex": '^06[0-9]{7,8}$'
    },
    "email": {
        "type": "string",
        "unique": True,
        "regex": '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    },
    "note": {
        "type": "string",
        "minlength": 10
    }
}
