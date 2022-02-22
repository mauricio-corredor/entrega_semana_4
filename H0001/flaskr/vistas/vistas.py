from tkinter.messagebox import NO
from flask import request
from flask_restful import Resource
import requests
from flaskr.Modelo.Pedido import Pedido
from flaskr.Modelo.Monolito import Monolito

class VistaNuevoPedido(Resource):

    def post(self):
        monolito = Monolito()        
        nuevo_pedido = Pedido(request.json["id_usuario"], request.json["id_proveedor"], request.json["id_producto"])        
        nuevo_pedido.inicializa_url()
        print("Usuario válido")
        
        if not monolito.producto_existe(nuevo_pedido.id_producto):
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


    



    

    

