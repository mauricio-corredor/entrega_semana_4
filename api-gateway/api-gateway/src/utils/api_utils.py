import json
import logging
from flask import Response, request
from werkzeug.exceptions import BadRequest, NotFound, InternalServerError


class ServerError(InternalServerError):
    name = ""
    description = ""


def http_bad_request(exception: BadRequest) -> Response:
    response = Response(response=json.dumps({
        "code": exception.code,
        "name": exception.name,
        "description": exception.description
    }),
        headers={"Content-Type": "application/json"},
        status=exception.code)
    return response


def http_not_found(exception: NotFound) -> Response:
    response = Response(response=json.dumps({
        "code": exception.code,
        "name": exception.name,
        "description": exception.description
    }),
        headers={"Content-Type": "application/json"},
        status=exception.code)
    return response


def internal_server_error_handler(exception: ServerError) -> Response:
    response = Response(response=json.dumps({
        "code": exception.code,
        "name": exception.name,
        "description": "Internal error"
    }),
        headers={"Content-Type": "application/json"},
        status=500)
    return response


def request_logger(requests: request) -> None:
    application_id = requests.headers.get('X-Application-Id', 'Unknown Source')
    logging.info(f'Incoming requests from: {application_id}')
