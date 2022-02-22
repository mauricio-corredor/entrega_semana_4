import logging

from flask_restful import Resource
import requests
from flask import request
from schema.request import RequestSchema
from services.session_service import SessionService
from services.login_service import LoginService
from services.orchestrator_order_query_service import OrchestratorOrderQueryService
from services.orchestrator_order_create_service import OrchestratorOrderCreateService
from settings import APP


request_schema = RequestSchema()


class Health(Resource):
    def get(self):
        return {"status": "ok"}, 200


class ApiGateway(Resource):
    def get(self, username: str, password: str, order_uuid: str) -> tuple:
        data = dict()
        data["username"] = username
        data["password"] = password
        data["order_uuid"] = order_uuid
        body = request_schema.validate(data=data)
        logging.info(f'{APP} logger UserRfm:'
                     f'start for user {body["username"]}')
        login_data = LoginService.login(
            body["username"],
            body["password"]
        )
        session = login_data["id"]
        session_data = SessionService.get_session(
            session
        )
        response = OrchestratorOrderQueryService.get_response(
            order_uuid=body["order_uuid"]
        )
        logging.info(f'{APP} logger UserRfm:'
                     f'done for user {body["username"]} '
                     f'response {response}')
        return response, 200

class ApiGateway2(Resource):
    def post(self) -> tuple:
       
        print(request.json["username"])
        #print("body: " +body)
        logging.info(f'{APP} logger UserRfm:'
                     f'start for user {request.json["username"]}')
        login_data = LoginService.login(
            request.json["username"],
            request.json["password"]

        )
        print(login_data)
        session = login_data["id"]

        session_data = SessionService.get_session(
            session
        )
        body = {"id_usuario": session_data["user_id"],"id_producto": request.json["id_producto"],"id_proveedor": request.json["id_proveedor"]}

        response = OrchestratorOrderCreateService.get_response(
            body=body
        )
        logging.info(f'{APP} logger UserRfm:'
                     f'done for user {body["id_usuario"]} '
                     f'response {response}')
        return response, 200