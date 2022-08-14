from core.strenum import StrEnum


class Roles(StrEnum):
    MEMBER = "member",
    COORDINATOR = "coordinator",
    PROJECT_MANAGER = "project_manager",
    ADMINISTRATOR = "administrator",


ROLES = [Roles.MEMBER, Roles.COORDINATOR,
         Roles.PROJECT_MANAGER, Roles.ADMINISTRATOR]
