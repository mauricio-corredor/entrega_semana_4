import logging
import traceback
import requests

import settings


class SessionService:
    @staticmethod
    def get_session(session: str):
        logging.info(f'{settings.APP} logger TicketChurnService'
                     f'get churn: start')
        URL = f"{settings.URL_MONOLITO}/sesion/{session}"
        try:
            logging.info(f'{settings.APP} logger TicketChurnService'
                         f'sent request: {URL}')
            r = requests.get(URL)
            data = r.json()

            logging.info(f'{settings.APP} logger TicketChurnService'
                         f'get topic: done {data}')
            return data
        except Exception as err:
            logging.warning('ADD DB ERROR: error={0} trace={1}'.format(
                err, " ".join(traceback.format_exc().splitlines()))
            )
