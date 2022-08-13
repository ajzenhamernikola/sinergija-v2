from schemas.project import PROJECT_SCHEMA

PROJECTS_DOMAIN = {
    "item_title": "Project",
    "resource_methods": ["GET", "POST"],
    "item_methods": ["GET", "PATCH"],
    "schema": PROJECT_SCHEMA
}
