from authorization.roles import Roles
from bson.objectid import ObjectId
from configs.domain_list import DomainList
from configs.jwt_payload_keys import JwtPayloadKeys
from core.request import SinergijaRequest
from eve import ID_FIELD, Eve
from hooks.base_hooks_table import BaseHooksTable


class PreGetHooksTable(BaseHooksTable):
    def on_pre_GET(self, resource, request: SinergijaRequest, lookup):
        if Roles.ADMINISTRATOR in request.auth[JwtPayloadKeys.ROLES]:
            return

        if resource == DomainList.COMMENTS:
            return
        if resource == DomainList.COMPANIES:
            return
        if resource == DomainList.CONTACTS:
            return
        if resource == DomainList.EVENTS:
            return
        if resource == DomainList.MESSAGES:
            lookup["room.people"] = {
                "$in": [request.auth[JwtPayloadKeys.USER_ID]]}
        if resource == DomainList.PEOPLE:
            lookup[ID_FIELD] = ObjectId(request.auth[JwtPayloadKeys.USER_ID])
        if resource == DomainList.PROJECTS:
            lookup["members"] = {"$in": [request.auth[JwtPayloadKeys.USER_ID]]}
        if resource == DomainList.ROOMS:
            lookup["people"] = {"$in": [request.auth[JwtPayloadKeys.USER_ID]]}
        if resource == DomainList.TASKS:
            lookup["$or"] = [
                {"assignees": {"$in": [request.auth[JwtPayloadKeys.USER_ID]]}},
                {"person": ObjectId(request.auth[JwtPayloadKeys.USER_ID])}
            ]
        if resource == DomainList.TEAMS:
            lookup["people"] = {"$in": [request.auth[JwtPayloadKeys.USER_ID]]}

    def register_hooks(self, app: Eve) -> None:
        app.on_pre_GET = self.on_pre_GET
