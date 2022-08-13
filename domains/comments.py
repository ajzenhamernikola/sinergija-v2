from schemas.comment import COMMENT_SCHEMA

COMMENTS_DOMAIN = {
    "item_title": "Comment",
    "resource_methods": ["GET", "POST"],
    "item_methods": ["GET", "PATCH", "DELETE"],
    "schema": COMMENT_SCHEMA
}
