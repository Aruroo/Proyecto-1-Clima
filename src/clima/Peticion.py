import json
import os
import requests
from datetime import datetime
class Peticion:

    def __init__(self, lat:float, lon:float, ciudadNombre):
        """Método que hace la petición a OpenWheather
            alt = float -la altitud de la ciudad a la que queremos solicitar el clima
            long = float -la longitud de la ciudad a la que queremos solicitar el clima
            ciudadNombre = string - la ciudad correspondiente a las coordenadas dadas
            TODO: Corregir la ruta absoluta por ruta relativa
        """
        try:
            #Leyendo la llave
            rutaLlave= open("key.txt", mode='r')
            llave=rutaLlave.read()
            rutaLlave.close()
        except FileNotFoundError:
            print("archivo de llave no encontrado")
        try:
            #Solicitando información
            url = 'https://api.openweathermap.org/data/2.5/weather?lat='+str(lat)+'&lon='+str(lon)+'&units=metric&lang=es&appid='+llave
            respuesta = requests.get(url)
            diccionarioCiudad = respuesta.json()
            ruta = "/caché/peticiones/"+ciudadNombre+".json"
            # Checando fecha y hora para saber cuando almacenar en el caché:
            fecha = datetime.now()
            #checando si el archivo existe en el caché:
            existeArchivo = os.path.isfile(ruta)
            if(existeArchivo):
                with open(ruta) as file:
                    info = json.load(file)
                    #Actualizamos el caché cada 3 minutos
                    if(info["minuto"]+3<fecha.minute):
                        diccionarioCiudad["minuto"] = fecha.minute #creemos una llave para minuto
                        self.creaArchivo(diccionarioCiudad,ruta)
            else:
                #guardamos la información que nos devolvió la request en un archivo
                diccionarioCiudad["minuto"] = fecha.minute #creemos una llave para minuto
                self.creaArchivo(diccionarioCiudad,ruta)

        except ConnectionError:
            print("solicitud rechazada")

    def creaArchivo(self,diccionarioCiudad,ruta):
        """Funcion auxiliar para crear archivo"""
        with open(ruta, "w") as i:
                    json.dump(diccionarioCiudad,i, indent=2)
