from http.client import FORBIDDEN

from authentication.base_jwt_auth import BaseJwtAuth
from flask import abort

from authorization.roles import ROLES, Roles


class RequireRoleAuth(BaseJwtAuth):
    def __init__(self, role: Roles) -> None:
        super().__init__()
        self.role = role

    def check_authentication(self, user_id, roles, allowed_roles, resource, method):
        if method == "GET":
            return True

        allow_for = ROLES[ROLES.index(self.role):]
        for role in roles:
            if role in allow_for:
                return True
        abort(FORBIDDEN, "You don't have privileged to access this resource")


class MemberRoleAuth(RequireRoleAuth):
    def __init__(self) -> None:
        super().__init__(Roles.MEMBER)


class CoordinatorRoleAuth(RequireRoleAuth):
    def __init__(self) -> None:
        super().__init__(Roles.COORDINATOR)


class ProjectManagerRoleAuth(RequireRoleAuth):
    def __init__(self) -> None:
        super().__init__(Roles.PROJECT_MANAGER)


class AdministratorRoleAuth(RequireRoleAuth):
    def __init__(self) -> None:
        super().__init__(Roles.ADMINISTRATOR)
