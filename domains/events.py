from authorization.role_based_access import CoordinatorRoleAuth
from schemas.event import EVENT_SCHEMA

EVENTS_DOMAIN = {
    "item_title": "Event",
    "resource_methods": ["GET", "POST"],
    "item_methods": ["GET", "PATCH", "DELETE"],
    "schema": EVENT_SCHEMA,
    "authentication": CoordinatorRoleAuth,
}
