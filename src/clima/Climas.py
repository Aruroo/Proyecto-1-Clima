import csv
import Ciudad

class Climas:

    def __init__(self):
        #Diccionario para almacenar datos de las ciudades.
        #Diccionario de las ciudades
        ciudades = {
            #Arreglo donde almacena los nombres de las ciudades.
            "nombres": [],

            #Arreglo donde almacena los objetos de tipo Ciudad.
            "coordenadas": []
            }
        self.ciudades= ciudades    

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

    def arregloNombres(self):
        """
            Devuelve un arreglo con los nombres de las ciudades.
        """
        return self.ciudades["nombres"]

    def arregloCiudades(self):
        """
            Devuelve un arreglo con los objetos de tipo Ciudad.
        """
        return self.ciudades["coordenadas"]

    def buscaCiudad(self,ciudad):
        """
            Función auxiliar que se encarga de realizar la búsqueda de coordenadas
            de la ciudad con base en su nombre pasado como parámetro, en el arreglo.
        """
        for i in range(1, len(self.arregloCiudades())):
            if ciudad == self.arregloNombres()[i]:
                return self.arregloCiudades()[i]
