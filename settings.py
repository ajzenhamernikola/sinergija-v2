import os

from configs.domain_list import DomainList
from domains.comments import COMMENTS_DOMAIN
from domains.companies import COMPANIES_DOMAIN
from domains.contacts import CONTACTS_DOMAIN
from domains.events import EVENTS_DOMAIN
from domains.people import PEOPLE_DOMAIN
from domains.projects import PROJECTS_DOMAIN
from domains.rooms import ROOMS_DOMAIN
from domains.tasks import TASKS_DOMAIN
from domains.teams import TEAMS_DOMAIN

# MongoDB configuration
if os.getenv("MONGO_URI"):
    MONGO_URI = os.getenv("MONGO_URI")
else:
    MONGO_HOST = os.getenv("MONGO_HOST")
    MONGO_PORT = int(os.getenv("MONGO_PORT"))
    MONGO_USERNAME = os.getenv("MONGO_USERNAME")
    MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
    MONGO_AUTH_SOURCE = os.getenv("MONGO_AUTH_SOURCE")
MONGO_DBNAME = os.getenv("MONGO_DBNAME")

# Domain configuration
DOMAIN = {
    DomainList.PEOPLE: PEOPLE_DOMAIN,
    DomainList.COMMENTS: COMMENTS_DOMAIN,
    DomainList.PROJECTS: PROJECTS_DOMAIN,
    DomainList.EVENTS: EVENTS_DOMAIN,
    DomainList.TEAMS: TEAMS_DOMAIN,
    DomainList.TASKS: TASKS_DOMAIN,
    DomainList.CONTACTS: CONTACTS_DOMAIN,
    DomainList.COMPANIES: COMPANIES_DOMAIN,
    DomainList.ROOMS: ROOMS_DOMAIN
}
