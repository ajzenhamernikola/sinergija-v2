from authorization.role_based_access import AdministratorRoleAuth
from schemas.contact import CONTACT_SCHEMA

CONTACTS_DOMAIN = {
    "item_title": "Contact",
    "resource_methods": ["GET", "POST"],
    "item_methods": ["GET", "PATCH", "DELETE"],
    "schema": CONTACT_SCHEMA,
    "authentication": AdministratorRoleAuth,
}
