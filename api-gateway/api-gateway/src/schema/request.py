import logging

from marshmallow import Schema, fields, ValidationError, EXCLUDE
from werkzeug.exceptions import BadRequest

from utils.profile_utils import profile
from settings import APP

"""
{
    "username": ,
    "password": ,
    "order_uuid":
    
}
"""


class RequestSchema(Schema):
    """Valida que la informacion de una solicitud este completa  y
    sea del tipo adecuado
    """
    order_uuid = fields.String(required=True, error="the order_uud"
                                                    "string is required",
                               allow_none=False)
    username = fields.String(required=True,
                             error="the username string is required",
                             allow_none=False)
    password = fields.String(required=True,
                             error="the password string is required",
                             allow_none=False)

    @profile
    def validate(self, data: dict, **kwargs) -> dict:
        """Valida el request contra el schema de la clase,
        retorna un BadRequest si falla con los detalles de donde fallo

        :rtype: dict
        """
        try:
            logging.info(f'{APP} logger validating data : {data}')
            tickets_data = self.load(data, unknown=EXCLUDE)
            return tickets_data

        except ValidationError as err:
            description_message = []
            for key, value in err.messages.items():
                logging.error(f'{key}: {value}')
                description_message.append(f'{key}: {value}')
            bad_request = BadRequest
            bad_request.description = ', '.join(description_message)
            logging.info(f'{APP} logger, RequestSchema.validate function:'
                         f'fail')
            raise bad_request
