from schemas.room import ROOM_SCHEMA

ROOMS_DOMAIN = {
    "item_title": "Room",
    "resource_methods": ["GET", "POST"],
    "item_methods": ["GET", "PATCH", "DELETE"],
    "soft_delete": True,
    "schema": ROOM_SCHEMA
}
