import logging
import traceback
import requests

import settings


class PaymentService:
    @staticmethod
    def get_payment(order_uuid: str):
        logging.info(f'{settings.APP} logger TicketTopicService'
                     f'get topic: start')
        URL = f"{settings.URL_PAYMENT}/payments/orders/{order_uuid}"
        try:
            logging.info(f'{settings.APP} logger TicketTopicService'
                         f'sent request: {URL}')
            r = requests.get(URL)
            data = r.json()

            logging.info(f'{settings.APP} logger TicketTopicService'
                         f'get topic: done {data}')
            return data
        except Exception as err:
            logging.warning('ADD DB ERROR: error={0} trace={1}'.format(
                err, " ".join(traceback.format_exc().splitlines()))
            )
