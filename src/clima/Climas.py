import csv
import Aeropuerto
from LectorIATA import LectorIATA

class Climas ():

    def __init__(self):
        """
            Clase Climas para crear un diccionario de aeropuertos leídos en un
            archivo .csv teniendo como formato columnas de IATA, coordenada latitud
            y coordenada altitud.
        """
        aeropuertos = {

            "nombres": [],

            "coordenadas": []
        }

        self.aeropuertos = aeropuertos
        sinPrimeraLinea = False

        with open('dataset1.csv') as f:
            lectorcsv = csv.reader(f)
            conjunto = {}
            conjunto = set()

            for fila in lectorcsv:
                if sinPrimeraLinea:
                    conjunto.add(fila[0])
                    conjunto.add(fila[1])
                sinPrimeraLinea = True

            sinPrimeraLinea = False

        with open('dataset1.csv') as f:
            lectorcsv = csv.reader(f)
            for fila in lectorcsv:
                if sinPrimeraLinea:
                    if fila[0] in conjunto:
                        lector = LectorIATA(fila[0])
                        nombreAeropuerto = lector.devuelveNombre()

                        if nombreAeropuerto != None:
                            aeropuertos["nombres"].append(fila[0] + ' (' + nombreAeropuerto + ')')
                        else:
                            aeropuertos["nombres"].append(fila[0])

                        aeropuertos["coordenadas"].append(Aeropuerto.Aeropuerto(fila[0], fila[2], fila[3]))
                        conjunto.discard(fila[0])

                    if fila[1] in conjunto:

                        lector = LectorIATA(fila[1])
                        nombreAeropuerto = lector.devuelveNombre()
                        if nombreAeropuerto != None:
                            aeropuertos["nombres"].append(fila[1] + ' (' + nombreAeropuerto + ')')
                        else:
                            aeropuertos["nombres"].append(fila[1])

                        aeropuertos["coordenadas"].append(Aeropuerto.Aeropuerto(fila[1], fila[4], fila[5]))
                        conjunto.discard(fila[1])

                sinPrimeraLinea = True

    def arregloNombres(self):
        """
            Devuelve un arreglo con los nombres de los aeropuertos.
        """
        return self.aeropuertos["nombres"]