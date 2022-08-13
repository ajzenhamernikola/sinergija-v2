from schemas.task import TASK_SCHEMA

TASKS_DOMAIN = {
    "item_title": "Task",
    "resource_methods": ["GET", "POST"],
    "item_methods": ["GET", "PATCH", "DELETE"],
    "schema": TASK_SCHEMA
}
