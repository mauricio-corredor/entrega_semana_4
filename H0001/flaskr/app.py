from flaskr import create_app
from flask_restful import Api
from .vistas import VistaNuevoPedido
from flask_cors import CORS, cross_origin
import os


app = create_app('default')
app_context = app.app_context()
app_context.push()

SECRET_KEY = os.getenv("MY_SECRET")



api = Api(app)
api.add_resource(VistaNuevoPedido, '/pedido')