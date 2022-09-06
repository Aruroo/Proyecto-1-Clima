import json
import requests
class Peticion:

    def __init__(self):
        """Método que hace la petición a OpenWheather
            TODO: Generalizar petición
            TODO: Procesar información
        """
        try:
            #Leyendo la llave
            rutaKey= open("key.txt", mode='r')
            key=rutaKey.read()
            rutaKey.close()

            url = 'https://api.openweathermap.org/data/2.5/weather?id=524901&lang=es&appid='+key
            respuesta = requests.get(url)
            contenido = respuesta.content
            archivo =open('clima.json','wb')
            archivo.write(contenido)
            archivo.close
            #info=json.loads(archivo)
        except FileNotFoundError:
            print("archivo no encontrado")
