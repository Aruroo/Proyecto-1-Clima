import csv
import Ciudad

class Clima ():

    #Diccionario de las ciudades
    ciudades = {
        #Arreglo donde almacena los nombres de las ciudades.
        "nombres": [],

        #Arreglo donde almacena los objetos de tipo Ciudad.
        "coordenadas": []
    }

    def __init__(self, ciudades):
        #Diccionario para almacenar datos de las ciudades.
        self.ciudades = ciudades

    #Variable que evita añadir la primera linea del archivo csv.
    b = False

    #Realiza el almacenamiento de los nombres en un conjunto para evitar repeticiones.
    with open('dataset1.csv') as f:
        reader = csv.reader(f)
        conjunto = {}
        conjunto = set()

        #Almacena los nombres de las ciudades en un conjunto donde no se repetirán
        #los nombres.
        for row1 in reader:
            if b:
                conjunto.add(row1[0])
                conjunto.add(row1[1])
            b = True

        b = False

    #Realiza el almacenamiento de las ciudades en el diccionario con base en el conjunto obtenido.
    with open('dataset1.csv') as f:
        reader = csv.reader(f)
        for row2 in reader:
            if b:
                #Revisa para la primer ciudad que aparece en la fila correspondiente en el .csv.
                if row2[0] in conjunto:
                    #Primer arreglo para los nombres.
                    ciudades["nombres"].append(row2[0])

                    #Segundo arreglo para objetos de tipo Ciudad.
                    ciudades["coordenadas"].append(Ciudad.Ciudad(row2[0], row2[2], row2[4]))
                    conjunto.discard(row2[0])

                #Revisa para la primer ciudad que aparece en la fila correspondiente en el .csv.
                if row2[1] in conjunto:
                    #Primer arreglo para los nombres.
                    ciudades["nombres"].append(row2[1])

                    #Segundo arreglo para objetos de tipo Ciudad.
                    ciudades["coordenadas"].append(Ciudad.Ciudad(row2[1], row2[3], row2[5]))
                    conjunto.discard(row2[1])
            b = True

    def arreglo_nombres():
        """
            Devuelve un arreglo con los nombres de las ciudades.
        """
        return ciudades["nombres"]

    def arreglo_ciudades():
        """
            Devuelve un arreglo con los objetos de tipo Ciudad.
        """
        return ciudades["coordenadas"]

    def procesa_petición(ciudad):
        """
            Método que se encarga de procesar la petición o bien, arrojar datos de
            la ciudad pasada como parámetro por el usuario.
        """

        """Busca en el diccionario las coordenadas"""
        coordenadasciudad = busca_ciudad(ciudad)

        """Revisar en caché: Bandera dada por la función auxiliar 2 para saber si
        la información solicitada se encuentra en caché. True si se encuentra la
        información en caché. False si no se encuentra la información en caché."""
        bandera1 = auxiliar(ciudad)

        if bandera1:
            """Devuelve el archivo .json que contiene los datos a recolectar necesarios."""

        else:
            """Realizar petición para devolver un archivo .json."""

    def busca_ciudad(ciudad):
        """
            Función auxiliar que se encarga de realizar la búsqueda de coordenadas
            de la ciudad con base en su nombre pasado como parámetro, en el arreglo.
        """
        for i in range(1, arreglo_ciudades().length()):
            if ciudad == arreglo_nombres()[i]:
                return arreglo_ciudades()[i]

    def auxiliar(ciudad):
        """
            Función auxiliar que se encarga de comprobar si la información de la
            ciudad dada comp parámetro se encuentra en caché. Devuelve True si se
            encuentra en caché o False si no está en caché.
        """
        return False

    def recolecta_info():
        """
            Método que se encarga de recolectar los datos necesarios del archivo
            .json dado por el método anterior.
        """
