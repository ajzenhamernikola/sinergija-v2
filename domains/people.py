from schemas.person import PERSON_SCHEMA

PEOPLE_DOMAIN = {
    "item_title": "Person",
    "resource_methods": ["GET", "POST"],
    "item_methods": ["GET", "PATCH", "DELETE"],
    "schema": PERSON_SCHEMA
}
