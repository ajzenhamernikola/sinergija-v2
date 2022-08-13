from schemas.team import TEAM_SCHEMA

TEAMS_DOMAIN = {
    "item_title": "Team",
    "resource_methods": ["GET", "POST"],
    "item_methods": ["GET", "PATCH", "DELETE"],
    "schema": TEAM_SCHEMA
}
