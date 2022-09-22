
import json

class LectorIATA():

    def __init__(self, iata):
        """
        Clase para obtener el nombre del aeropuerto dada su clave IATA.
        
        iata = String - El código IATA de la ciudad.
        """
        self.__ruta = "IATACodes.json"

        with open(self.__ruta) as file:
            archivoIATA = json.load(file)
            ciudadDatos = archivoIATA[iata]
            self.__info = str(ciudadDatos["name"]) +"," + str(ciudadDatos["iso"])
    
    def devuelveNombre(self):
        """
        Devuelve el nombre del aeropuerto.
        "None" si no se cuenta con su nombre.
        """
        return self.__info

