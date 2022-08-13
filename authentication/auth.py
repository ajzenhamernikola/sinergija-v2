from datetime import timedelta
from http.client import NOT_FOUND, UNPROCESSABLE_ENTITY

from configs.domain_list import DomainList
from core.jwt import AccessTokenJwtEncoder, RefreshTokenJwtEncoder
from flask import Blueprint, abort
from flask import current_app as app
from flask import make_response, request

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.post("/login")
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    if not username:
        abort(UNPROCESSABLE_ENTITY, "Username is required")
    if not password:
        abort(UNPROCESSABLE_ENTITY, "Password is required")

    people = app.data.driver.db[DomainList.PEOPLE]
    person = people.find_one({"username": username})

    if not person:
        abort(NOT_FOUND, "User with the requested username does not exist")

    jwt_payload = {
        "userId": str(person["_id"]),
        "roles": person["roles"]
    }
    response = make_response(
        {"access_token": AccessTokenJwtEncoder().encode(jwt_payload)})

    refresh_token_encoder = RefreshTokenJwtEncoder()

    response.set_cookie("refresh_token", refresh_token_encoder.encode(jwt_payload), max_age=timedelta(
        seconds=refresh_token_encoder.get_duration_in_seconds()), secure=True, httponly=True)

    return response
