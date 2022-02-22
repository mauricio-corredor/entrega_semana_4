import logging
import traceback
import requests

import settings


class LoginService:
    @staticmethod
    def login(username: str, password: str):
        logging.info(f'{settings.APP} logger TicketTopicService'
                     f'get topic: start')
        URL = f"{settings.URL_MONOLITO}/login"
        params = dict(
            username=username,
            password=password,
        )
        try:
            logging.info(f'{settings.APP} logger TicketTopicService'
                         f'sent request: {URL}')
            r = requests.post(URL, json=params)
            data = r.json()

            logging.info(f'{settings.APP} logger TicketTopicService'
                         f'get topic: done {data}')
            return data
        except Exception as err:
            logging.warning('ADD DB ERROR: error={0} trace={1}'.format(
                err, " ".join(traceback.format_exc().splitlines()))
            )
