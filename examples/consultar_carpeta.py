import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from WatanaApi.watana import *

ruta = 'https://api.watana.pe/api/v1/proveedor/4-qMbLHOJvadmOhVK7z6d-A_nfqAKvK68C7zlJ02g-Q'
token = 'eyJhbGciOiJIUzI1NiJ9.eyJ0b2tlbiI6ImFlNDg3NjU5NDc3ZmNhNDE1YmNhNzgyMWQ3NzlkNzU1ZGQ5M2YzOWYyYjJiNTUzNyJ9.GfB2Q7GTeHndh0CHJ2i3GHtO1hzNT9gch_6JLKMbp9g'

# Crear una instancia de WatanaApi
api = WatanaApi(ruta, token)


# Crear el diccionario de datos
data = {
    'carpeta_codigo': 'DOC001'
}

# Llamar a la función consultar_carpeta
try:
    response = api.consultar_carpeta(data)
    print(response)
except Exception as e:
    print(str(e))
    
