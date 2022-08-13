from core.strenum import StrEnum


class JwtPayloadKeys(StrEnum):
    USER_ID = "user_id",
    ROLES = "roles",
    EXPIRES_AT = "exp",
