import csv
import Ciudad

class Clima ():

    ciudades = []

    def __init__(self, ciudades):
        #Arreglo para almacenar datos de tipo Ciudad.
        self.ciudades = ciudades

    with open('ciudades.csv') as f:
        """
            Almacena los datos del csv en un arreglo con datos de tipo Ciudad.
        """
        reader = csv.reader(f)
        for row1 in reader:
            nombre1 = row1[0]
            #Datos de la ciudad 1.
            ciudad1 = Ciudad.Ciudad(row1[0], row1[2], row1[4])

            #Añade la información de la nueva ciudad.
            ciudades.append(ciudad1)

            for row2 in reader:
                nombre2 = row2[1]

                if nombre1 != nombre2:
                    #Datos de la ciudad 2.
                    ciudad2 = Ciudad.Ciudad(row2[1], row2[3],row2[5])

                    #Añade la información de la nueva ciudad.
                    ciudades.append(ciudad2)

    def método1():
        """
            Método que se encarga de procesar la petición o bien, arrojar datos de
            la ciudad dada por el usuario en la interfaz
        """

        """Ciudad de destino dado por el usuario (nombre): ciudaddestino"""
        #ciudaddestino = ...

        """Busca en el diccionario las coordenadas"""
        coordenadasciudad = funciónAux(ciudaddestino)

        """Revisar en caché: Bandera dada por la función auxiliar 2 para saber si
        la información solicitada se encuentra en caché. True si se encuentra la
        información en caché. False si no se encuentra la información en caché."""
        bandera1 = funciónAux2(ciudaddestino)

        if bandera1:
            """Devuelve el archivo .json que contiene los datos a recolectar necesarios."""

        else:
            """Realizar petición para devolver un archivo .json."""


    def funciónAux(ciudad):
        """
            Función auxiliar que se encarga de realizar la búsqueda de coordenadas
            de la ciudad con base en su nombre pasado como parámetro, en el arreglo.
        """
        for i in range(1, ciudades.length()):
            if ciudad == ciudades[i].nombre:
                return ciudades[i]

    def funciónAux2(ciudad):
        """
            Función auxiliar que se encarga de comprobar si la información de la
            ciudad dada comp parámetro se encuentra en caché. Devuelve True si se
            encuentra en caché o False si no está en caché.
        """
        return False

    def método2():
        """
            Método que se encarga de recolectar los datos necesarios del archivo
            .json dado por el método anterior.
        """
