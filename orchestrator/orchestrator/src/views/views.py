import logging

from flask_restful import Resource

from services.product_service import ProductService
from services.order_service import OrderService
from services.seller_service import SellerService
from services.agenda_service import AgendaService
from services.payment_service import PaymentService
from settings import APP


class Health(Resource):
    def get(self):
        return {"status": "ok"}, 200


class OrchestratorQueryOrder(Resource):
    def get(self, order_uuid: str) -> tuple:
        logging.info(f'{APP} logger UserRfm:'
                     f'start for user {order_uuid}')
        order_data = OrderService.get_order(
            order_uuid=order_uuid
        )
        product_id = order_data["itemId"]
        product_data = ProductService.get_product(
            product_id=product_id
        )
        seller_uuid = order_data["sellerId"]
        seller_data = SellerService.get_seller(
            seller_uuid=seller_uuid
        )
        agenda_data = AgendaService.get_agenda(
            seller_uuid=seller_uuid,
            order_uuid=order_uuid
        )
        payment_data = PaymentService.get_payment(
            order_uuid=order_uuid
        )
        response = dict(

            order_data=order_data,
            product_data=product_data,
            seller_data=seller_data,
            agenda_data=agenda_data,
            payment_data=payment_data
        )
        logging.info(f'{APP} logger UserRfm:'
                     f'response {response}')
        return response, 200
