import requests
import os


class Monolito:

    def __init__(self):
             
       self.UrlMonolito = os.getenv("URL_MONOLITO")

    def ObtenerIdUsuario(self, username, password):
  
        try:
            idSesion = self.ObtenerIdSesion(username, password)
            if not idSesion is None:
                return self.validarSesion(idSesion)
            return None
        except:
            return None

    def ObtenerIdSesion(self, username, password):
        try:
            print(self.UrlMonolito)
            login = requests.post(self.UrlMonolito + "login", json = {"username": username, "password": password})   
            if login.status_code == 200:
                data = login.json()
                return data['id']
            return None
        except:
            return None

    def validarSesion(self, id_sesion):
        try:
            url = self.UrlMonolito + 'sesion/' + id_sesion
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
            url = self.UrlMonolito + 'producto/' + id_producto
            sesion = requests.get(url)
            if sesion.status_code == 200:     
                return True
            return False
        except:
            return False