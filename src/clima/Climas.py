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
        #Diccionario de aeropuertos.
        aeropuertos = {
            #Arreglo donde almacena las IATA's y/o nombres de los aeropuertos.
            "nombres": [],

            #Arreglo donde almacena los objetos de tipo Aeropuerto.
            "coordenadas": []
        }
        self.aeropuertos = aeropuertos

        #Variable que evita añadir la primera linea del archivo csv.
        sinPrimeraLinea = False

        archivo = '../datos/dataset1.csv'
        self.archivo = archivo

        self.sinPrimeraLinea = sinPrimeraLinea

        conjunto = {}
        conjunto = set()
        conjunto = self.conjuntoNombres()

        with open(archivo) as f:
            """
                Realiza el almacenamiento de datos en el diccionario con base en el conjunto obtenido.
            """
            lectorcsv = csv.reader(f)
            for fila in lectorcsv:
                if self.sinPrimeraLinea:
                    #Revisa para el primer aeropuerto que aparece en la fila correspondiente en el .csv.
                    if fila[0] in conjunto:

                        lector = LectorIATA(fila[0])
                        nombreAeropuerto = lector.devuelveNombre()

                        #Primer arreglo para las IATA's y/o nombres.
                        if nombreAeropuerto != None:
                            aeropuertos["nombres"].append(fila[0] + ' (' + nombreAeropuerto + ')')
                        else:
                            aeropuertos["nombres"].append(fila[0])

                        #Segundo arreglo para objetos de tipo Aeropuerto.
                        aeropuertos["coordenadas"].append(Aeropuerto.Aeropuerto(fila[0], fila[2], fila[3]))

                        #Elimina al nombre del conjunto para evitar introducir nuevamente
                        #el mismo aeropuerto en el diccionario.
                        conjunto.discard(fila[0])

                    #Revisa para el segundo aeropuerto que aparece en la fila correspondiente en el .csv.
                    if fila[1] in conjunto:

                        lector = LectorIATA(fila[1])
                        nombreAeropuerto = lector.devuelveNombre()

                        #Primer arreglo para las IATA's y/o nombres.
                        if nombreAeropuerto != None:
                            aeropuertos["nombres"].append(fila[1] + ' (' + nombreAeropuerto + ')')
                        else:
                            aeropuertos["nombres"].append(fila[1])

                        #Segundo arreglo para objetos de tipo Aeropuerto.
                        aeropuertos["coordenadas"].append(Aeropuerto.Aeropuerto(fila[1], fila[4], fila[5]))

                        #Elimina al nombre del conjunto para evitar introducir nuevamente
                        #el mismo aeropuerto en el diccionario.
                        conjunto.discard(fila[1])

                self.sinPrimeraLinea = True

    def conjuntoNombres(self):
        """
            Realiza el almacenamiento de las IATA's de los aeropuertos para devolver
            un conjunto y evitar repeticiones de IATA's.
        """
        f = open(self.archivo)
        lectorcsv = csv.reader(f)
        conjunto = {}
        conjunto = set()

        for fila in lectorcsv:
            if self.sinPrimeraLinea:
                conjunto.add(fila[0])
                conjunto.add(fila[1])
            self.sinPrimeraLinea = True

        self.sinPrimeraLinea = False

        return conjunto

    def arregloNombres(self):
        """
            Devuelve un arreglo con los nombres de los aeropuertos.
        """
        return self.aeropuertos["nombres"]

    def arregloAeropuertos(self):
        """
            Devuelve un arreglo con los objetos de tipo Aeropuerto.
        """
        return self.aeropuertos["coordenadas"]

    def buscaAeropuerto(self,aeropuerto):
        """
            Función que se encarga de realizar la búsqueda en el arreglo de objetos
            de tipo Aeropuerto con base en el nombre o IATA pasado como parámetro.
        """
        for i in range(1, len(self.arregloAeropuertos())):
            if aeropuerto == self.arregloNombres()[i]:
                return self.arregloAeropuertos()[i]
