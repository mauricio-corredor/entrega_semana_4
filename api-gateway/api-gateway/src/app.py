import logging

from flask import Flask
from flask_restful import Api
from waitress import serve
from signalfx_tracing import auto_instrument, create_tracer

from views.views import Health, ApiGateway, ApiGateway2
import settings

tracer = create_tracer(access_token=settings.SIGNALFX_ACCESS_TOKEN,
                       config={
                           'service_name': settings.SIGNALFX_SERVICE_NAME,
                           'jaeger_endpoint': settings.SIGNALFX_ENDPOINT_URL
                       })

auto_instrument(tracer)


def create_app():
    app = Flask(__name__)
    app.config['PROPAGATE_EXCEPTIONS'] = True
    return app


logging.basicConfig(format=settings.LOG_PATTERN, level=logging.INFO)

app = create_app()
app_context = app.app_context()
app_context.push()

api = Api(app)
api.add_resource(Health, '/health')
api.add_resource(ApiGateway, '/order_query')
api.add_resource(ApiGateway2, '/order_create')


if __name__ == "__main__":
    logging.info(f'{settings.APP} Server started')
    serve(
        app=app,
        host='0.0.0.0',
        port=8000,
        threads=settings.WAITRESS_WORKERS,
        connection_limit=settings.WAITRESS_CHANNELS,
    )
