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
            ruta = "../caché/"+ciudadNombre+".json"
            #checando si el archivo existe en el caché:
            existeArchivo = os.path.isfile(ruta)
            if(existeArchivo):
                with open(ruta) as file:
                    info = json.load(file)
                    #Actualizamos el caché cada 5 minutos
                    if(Peticion.__necesitaActualizarse(self, fechas=info)):
                        fecha = datetime.now()
                        diccionarioCiudad["ano"] = fecha.year
                        diccionarioCiudad["mes"] = fecha.month                    
                        diccionarioCiudad["dia"] =fecha.day
                        diccionarioCiudad["hora"] =fecha.hour
                        diccionarioCiudad["minuto"] =fecha.minute
                        self.__creaArchivo(diccionarioCiudad, ruta)
            else:
                # Checando fecha y hora para saber cuando almacenar en el caché:
                fecha = datetime.now()
                diccionarioCiudad["ano"] = fecha.year
                diccionarioCiudad["mes"] = fecha.month                    
                diccionarioCiudad["dia"] =fecha.day
                diccionarioCiudad["hora"] =fecha.hour
                diccionarioCiudad["minuto"] =fecha.minute
                #guardamos la información que nos devolvió la request en un archivo
                self.__creaArchivo(diccionarioCiudad, ruta)

        except ConnectionError:
            print("solicitud rechazada")

    def __creaArchivo(self,diccionarioCiudad,ruta):
        """Funcion para crear archivo"""
        with open(ruta, "w") as i:
                    json.dump(diccionarioCiudad,i, indent=2)

    def __necesitaActualizarse(self, fechas:dict):
        """
        Método auxiliar que indica cuando es necesario
        actualizar el archivo en el caché.

        fechas: un diccionario con las llaves:
        "año", "mes", "dia", "hora", "minuto"
        """
        actual = datetime.now()
        año = actual.year
        mes = actual.month
        dia = actual.day
        hora = actual.hour
        minuto = actual.minute

        if(año != fechas["ano"]):
            return True
        if(mes != fechas["mes"]):
            return True
        if(dia != fechas["dia"]):
            return True
        if(hora != fechas["hora"]):
            return True
        if(minuto > fechas["minuto"]+5):
            return True
        return False  