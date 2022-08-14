from http.client import UNAUTHORIZED

from configs.jwt_payload_keys import JwtPayloadKeys
from core.jwt import JwtDecoder
from db.collections.people import PeopleMongoOperations
from eve.auth import TokenAuth
from flask import abort


class BaseJwtAuth(TokenAuth):
    def check_auth(self, token, allowed_roles, resource, method):
        try:
            payload = JwtDecoder().decode(token)
        except:
            abort(UNAUTHORIZED, "JWT cannot be validated")

        person = PeopleMongoOperations().find_by_id(
            payload[JwtPayloadKeys.USER_ID])
        if not person:
            abort(UNAUTHORIZED, "User not found")

        return self.check_authentication(payload[JwtPayloadKeys.USER_ID], payload[JwtPayloadKeys.ROLES], allowed_roles, resource, method)

    def check_authentication(self, user_id, roles, allowed_roles, resource, method):
        return True
