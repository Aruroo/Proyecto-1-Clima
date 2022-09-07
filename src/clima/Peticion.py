import json
import requests
class Peticion:

    def __init__(self, lat, lon):
        """Método que hace la petición a OpenWheather
            alt = float -la altitud de la ciudad a la que queremos solicitar el clima
            long = float -la longitud de la ciudad a la que queremos solicitar el clima 
        """
        try:
            #Leyendo la llave
            rutaLlave= open("key.txt", mode='r')
            llave=rutaLlave.read()
            rutaLlave.close()
            #Solicitando información
        except FileNotFoundError:
            print("archivo de llave no encontrado")    
        try:
            url = 'https://api.openweathermap.org/data/2.5/weather?lat='+str(lat)+'&lon='+str(lon)+'&units=metric&lang=es&appid='+key
            respuesta = requests.get(url)
            diccionarioCiudad = respuesta.json()
            nombreArchivo = diccionarioCiudad["name"]
            #guardamos la información que nos devolvió la request en un archivo
            with open("/home/arturo/Python projects/src/caché/peticiones/"+nombreArchivo+".json", "w") as i:
                json.dump(diccionarioCiudad,i, indent=2)
        except ConnectionError:
            print("solicitud rechazada")        
           


#pedir = Peticion(25.7785,-100.107)