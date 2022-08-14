from authorization.role_based_access import MemberRoleAuth
from schemas.message import MESSAGE_SCHEMA

MESSAGES_DOMAIN = {
    "item_title": "Message",
    "resource_methods": ["GET", "POST"],
    "item_methods": ["GET", "PATCH", "DELETE"],
    "soft_delete": True,
    "schema": MESSAGE_SCHEMA,
    "authentication": MemberRoleAuth,
}
