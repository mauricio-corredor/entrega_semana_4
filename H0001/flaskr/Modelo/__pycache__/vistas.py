from tkinter.messagebox import NO
from flask import request
from flask_restful import Resource
from flask import request
import requests
from flaskr.Modelo.Pedido import Pedido


class VistaNuevoPedido(Resource):

    def post(self):
        nuevo_pedido = Pedido(request.json["id_sesion"], request.json["id_proveedor"], request.json["id_producto"])
        print(nuevo_pedido.id_sesion + " " + nuevo_pedido.id_proveedor + " " + nuevo_pedido.id_producto)

        get_id_usuario= consumo_servicios().sesion_existe(nuevo_pedido.id_sesion)
        nuevo_pedido.id_usuario = get_id_usuario

        if get_id_usuario  is None:
            return 'Sesion no valida',404
        print("Usuario válido")
        
        if not consumo_servicios().producto_existe(nuevo_pedido.id_producto):
            return 'Producto no existe',404
        print("Producto existe")

        get_status_proveedor= nuevo_pedido.proveedor_disponible()
        print("Status proveedor: " +  get_status_proveedor)
        #if get_status_proveedor  == "false" or get_status_proveedor is None:
        #    return 'Provedor no disponible',404
        print("Proveedor disponible")
        
        if not nuevo_pedido.crear_order():
            return "Pedido Rechazado", 404
        print("Order ID: " + nuevo_pedido.id_order)

        if not nuevo_pedido.crear_agenda():
            nuevo_pedido.elimina_order()
            return "Pedido Rechazado", 404
        print("Agenda creada")

        if not nuevo_pedido.crear_pago():
            nuevo_pedido.elimina_agenda()
            nuevo_pedido.elimina_order()
            return "Pedido Rechazado", 404
        print("Pago creada")

        return 'Pedido Realizado'

class consumo_servicios():

    def sesion_existe(self, id_sesion):
        try:
            url = 'http://127.0.0.1:5000/sesion/'+id_sesion
            sesion = requests.get(url)

            if sesion.status_code == 200:
                data = sesion.json()
                valor_id_usuario = data['user_id']
                return valor_id_usuario

            return None

        except:
            return None

    def producto_existe(self, id_producto):
        try:
            url = 'http://127.0.0.1:5000/producto/'+id_producto
            sesion = requests.get(url)

            if sesion.status_code == 200:
     
                return True
            return False

        except:
            return False



    

    

