from typing import Any

from configs.jwt_payload_keys import JwtPayloadKeys
from flask import Request


class SinergijaRequest(Request):
    def __init__(self, environ: Any, populate_request: bool = True, shallow: bool = False) -> None:
        super().__init__(environ, populate_request, shallow)
        self.auth = {
            JwtPayloadKeys.USER_ID: None,
            JwtPayloadKeys.ROLES: None,
        }
