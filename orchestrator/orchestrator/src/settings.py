import os
import datetime as dt

from werkzeug.security import generate_password_hash

# APP
APP = 'a-tormentados app'
APP_VERSION = "0.2.0"
X_APPLICATION_ID = os.getenv('x_application_id', APP)
DEFAULT_TIMEOUT = int(os.getenv('DEFAULT_TIMEOUT', 4))
DEPLOYED_AT = dt.datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S")
DEBUG = os.getenv('DEBUG', False)
LOG_PATTERN = '%(asctime)s.%(msecs)s:%(name)s:%(thread)d:(%(threadName)-10s)' \
              ':%(levelname)s:%(process)d:%(message)s'

# URLs
URL_MONOLITO = os.getenv('URL_MONOLITO', 'localhost')
URL_ORDER = os.getenv('URL_ORDER', 'localhost')
URL_SELLER = os.getenv('URL_SELLER', 'localhost')
URL_AGENDA = os.getenv('URL_AGENDA', 'localhost')
URL_PAYMENT = os.getenv('URL_PAYMENT', 'localhost')

# WAITRESS CONFIG
WAITRESS_WORKERS = int(os.getenv('WAITRESS_WORKERS', 8))
WAITRESS_CHANNELS = int(os.getenv('WAITRESS_CHANNELS', 100))

# SIGNALFX
SIGNALFX_ACCESS_TOKEN = os.getenv('SIGNALFX_ACCESS_TOKEN', '')
SIGNALFX_ENDPOINT_URL = os.getenv('SIGNALFX_ENDPOINT_URL', '')
SIGNALFX_TRACING_ENABLED = os.getenv('SIGNALFX_TRACING_ENABLED', False)
SIGNALFX_SERVICE_NAME = f'{APP}'
