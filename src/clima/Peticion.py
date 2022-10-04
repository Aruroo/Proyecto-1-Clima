import json
import os
import requests
from datetime import datetime
class Peticion:

    def __init__(self, lat:float, lon:float, AeropuertoNombre):
        """Método que hace la petición a OpenWheather

            alt = float -la altitud del aeropuerto a la que queremos solicitar el clima

            long = float -la longitud del aeropuerto a la que queremos solicitar el clima

            aeropuertoNombre = string - el aeropuerto correspondiente a las coordenadas dadas

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
            diccionarioAeropuerto = respuesta.json()
            ruta = "../caché/"+AeropuertoNombre+".json"
            #checando si el archivo existe en el caché:
            existeArchivo = os.path.isfile(ruta)
            if(existeArchivo):
                with open(ruta) as file:
                    info = json.load(file)
                    #Actualizamos el caché cada 5 minutos
                    if(Peticion.__necesitaActualizarse(self, fechas=info)):
                        fecha = datetime.now()
                        diccionarioAeropuerto["ano"] = fecha.year
                        diccionarioAeropuerto["mes"] = fecha.month
                        diccionarioAeropuerto["dia"] =fecha.day
                        diccionarioAeropuerto["hora"] =fecha.hour
                        diccionarioAeropuerto["minuto"] =fecha.minute
                        self.__creaArchivo(diccionarioAeropuerto, ruta)
            else:
                # Checando fecha y hora para saber cuando almacenar en el caché:
                fecha = datetime.now()
                diccionarioAeropuerto["ano"] = fecha.year
                diccionarioAeropuerto["mes"] = fecha.month
                diccionarioAeropuerto["dia"] =fecha.day
                diccionarioAeropuerto["hora"] =fecha.hour
                diccionarioAeropuerto["minuto"] =fecha.minute
                #guardamos la información que nos devolvió la request en un archivo
                self.__creaArchivo(diccionarioAeropuerto, ruta)

        except ConnectionError:
            print("solicitud rechazada")

    def __creaArchivo(self,diccionarioAeropuerto,ruta):
        """Funcion para crear archivo"""
        with open(ruta, "w") as i:
                    json.dump(diccionarioAeropuerto,i, indent=2)

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
