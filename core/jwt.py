import os
from abc import abstractmethod
from datetime import datetime, timedelta, timezone
from typing import Any, Dict

import jwt


class JwtEncoder:
    def encode(self, payload: Dict[str, Any]) -> str:
        payload["exp"] = datetime.now(
            tz=timezone.utc) + timedelta(seconds=self.get_duration_in_seconds())
        return jwt.encode(payload, os.getenv("SINERGIJA_JWT_SECRET"), "HS256")

    @abstractmethod
    def get_duration_in_seconds(self):
        pass


class JwtDecoder:
    def decode(self, encoded_jwt: str) -> Dict[str, Any]:
        return jwt.decode(encoded_jwt, os.getenv("SINERGIJA_JWT_SECRET"), "HS256")


class AccessTokenJwtEncoder(JwtEncoder):
    def get_duration_in_seconds(self):
        return int(os.getenv("SINERGIJA_ACCESS_TOKEN_VALIDITY")) * 60


class RefreshTokenJwtEncoder(JwtEncoder):
    def get_duration_in_seconds(self):
        return int(os.getenv("SINERGIJA_REFRESH_TOKEN_VALIDITY")) * 30 * 24 * 60 * 60
