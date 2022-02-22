import logging
import traceback
import requests

import settings


class OrchestratorOrderCreateService:
    @staticmethod
    def get_response(body: dict):
        logging.info(f'{settings.APP} logger TicketChurnService'
                     f'get churn: start')
        URL = f"{settings.URL_ORDER_CREATE}/pedido"
        try:
            logging.info(f'{settings.APP} logger TicketChurnService'
                         f'sent request: {URL}')
            r = requests.post(URL, json=body)
            data = r.json()

            logging.info(f'{settings.APP} logger TicketChurnService'
                         f'get topic: done {data}')
            return data
        except Exception as err:
            logging.warning('ADD DB ERROR: error={0} trace={1}'.format(
                err, " ".join(traceback.format_exc().splitlines()))
            )
