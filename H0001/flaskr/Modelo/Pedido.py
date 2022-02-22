import requests
import os
from configparser import ConfigParser

class Pedido:
    def __init__(self, id_usuario, id_proveedor, id_producto):
        self.id_proveedor = id_proveedor
        self.id_producto = id_producto
        self.id_usuario = id_usuario
        self.id_order = ""
        self.id_pago = ""
        self.url_agenda = ""
        self.url_order = ""
        self.url_proveedor = ""
        self.url_pago = ""

    def inicializa_url(self):

        self.url_agenda =  os.getenv("URL_AGENDA")   
        self.url_order =  os.getenv("URL_ORDER")
        self.url_proveedor =  os.getenv("URL_PROVEEDOR")
        self.url_pago =  os.getenv("URL_PAGO")

    def proveedor_disponible(self):
        try:
            url = self.url_proveedor + self.id_proveedor
            proveedor = requests.get(url)
            if proveedor.status_code == 200:
                data = proveedor.json()
                return data['isActive']
            return None
        except:
            return None

    def crear_order(self):
        try:
            order_response = requests.post(self.url_order, json = {"item": {"uuid": self.id_producto }, "seller": {"uuid": self.id_proveedor},"user": {"uuid": self.id_usuario } })   
            if order_response.status_code == 201:
                data = order_response.json()
                self.id_order = data['orderId']
                return True
            return False
        except:
            return False
    
    def crear_agenda(self):
        try:
            order_response = requests.post(self.url_agenda + 'sellers/' + self.id_order, json = {"uuid": self.id_order })   
            if order_response.status_code == 201:
                return True
            return False
        except:
            return False

    def elimina_order(self):
        try:
            order_response = requests.delete(self.url_order + self.id_order)   
            if order_response.status_code == 200:
                return True
            return False
        except:
            return False

    def crear_pago(self):
        try:
            order_response = requests.post(self.url_pago, json = {"order": {"uuid": self.id_order},"user": {"uuid": self.id_usuario } })   
            if order_response.status_code == 201:
                data = order_response.json()
                self.id_pago = data['paymentId']
                return True
            return False
        except:
            return False

    def elimina_agenda(self):
        try:
            order_response = requests.delete(self.url_agenda + 'sellers/' + self.id_proveedor + "/order/" + self.id_order)   
            if order_response.status_code == 200:
                return True
            return False
        except:
            return False