from authorization.roles import ROLES, Roles

PERSON_SCHEMA = {
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
        "required": True,
        "minlength": 9,
        "maxlength": 10,
        "regex": '^06[0-9]{7,8}$'
    },
    "email": {
        "type": "string",
        "required": True,
        "unique": True,
        "regex": '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    },
    "username": {
        "type": "string",
        "required": True,
        "unique": True
    },
    "password": {
        "type": "string",
        "required": True
    },
    "profile_picture": {
        "type": "media",
        "required": True
    },
    "roles": {
        "type": "list",
        "required": True,
        "default": [Roles.MEMBER],
        "allowed": ROLES
    }
}
