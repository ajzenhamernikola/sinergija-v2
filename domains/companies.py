from authorization.role_based_access import AdministratorRoleAuth
from schemas.company import COMPANY_SCHEMA

COMPANIES_DOMAIN = {
    "item_title": "Company",
    "resource_methods": ["GET", "POST"],
    "item_methods": ["GET", "PATCH", "DELETE"],
    "schema": COMPANY_SCHEMA,
    "authentication": AdministratorRoleAuth,
}
