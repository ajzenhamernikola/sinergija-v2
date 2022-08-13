from datetime import timedelta
from http.client import NOT_FOUND, UNPROCESSABLE_ENTITY

from bson.objectid import ObjectId
from configs.domain_list import DomainList
from configs.jwt_payload_keys import JwtPayloadKeys
from core.jwt import AccessTokenJwtEncoder, JwtDecoder, RefreshTokenJwtEncoder
from flask import Blueprint, Response, abort
from flask import current_app as app
from flask import make_response, request
from jwt.exceptions import DecodeError, ExpiredSignatureError

bp = Blueprint("auth", __name__, url_prefix="/auth")


def generate_auth_response(person) -> Response:
    jwt_payload = {
        JwtPayloadKeys.USER_ID: str(person["_id"]),
        JwtPayloadKeys.ROLES: person["roles"]
    }
    response = make_response(
        {"access_token": AccessTokenJwtEncoder().encode(jwt_payload)})

    refresh_token_encoder = RefreshTokenJwtEncoder()

    response.set_cookie("refresh_token", refresh_token_encoder.encode(
        jwt_payload), samesite='None', secure=True, httponly=True, expires=jwt_payload[JwtPayloadKeys.EXPIRES_AT])

    return response


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

    return generate_auth_response(person)


@bp.post("/refresh")
def refresh():
    encoded_refresh_token = request.cookies.get("refresh_token")

    if not encoded_refresh_token:
        abort(401, "'refresh_token' cookie is not set")

    try:
        refresh_token_payload = JwtDecoder().decode(encoded_refresh_token)
    except ExpiredSignatureError:
        abort(401, "'refresh_token' cookie is expired, please log in again")
    except DecodeError:
        abort(401, "'refresh_token' validation failed")

    people = app.data.driver.db[DomainList.PEOPLE]
    person = people.find_one(
        {"_id": ObjectId(refresh_token_payload[JwtPayloadKeys.USER_ID])})

    if not person:
        abort(401, "User does not exist")

    return generate_auth_response(person)
