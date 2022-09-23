import csv
import Ciudad

class Climas ():

    def __init__(self):
        #Diccionario para almacenar datos de las ciudades.
        #Diccionario de ciudades.
        ciudades = {
        #Arreglo donde almacena los nombres de las ciudades.
        "nombres": [],

        #Arreglo donde almacena los objetos de tipo Ciudad.
        "coordenadas": []
        }
        self.ciudades = ciudades

        #Variable que evita añadir la primera linea del archivo csv.
        b = False

        with open('../datos/dataset1.csv') as f:
            """
                Realiza el almacenamiento de los nombres de las ciudades en un conjunto para evitar
                repeticiones.
            """
            reader = csv.reader(f)
            conjunto = {}
            conjunto = set()

            for row1 in reader:
                if b:
                    conjunto.add(row1[0])
                    conjunto.add(row1[1])
                b = True

            b = False

        with open('../datos/dataset1.csv') as f:
            """
                Realiza el almacenamiento de datos en el diccionario con base en el conjunto obtenido.
            """
            reader = csv.reader(f)
            for row2 in reader:
                if b:
                    #Revisa para la primer ciudad que aparece en la fila correspondiente en el .csv.
                    if row2[0] in conjunto:
                        if row2[0] == 'TLC':
                            cadenaciudad = row2[0] + ' (Toluca, Estado de México, México)'
                        elif row2[0] == 'MTY':
                            cadenaciudad = row2[0] + ' (Monterrey, Nuevo León, México)'
                        elif row2[0] == 'MEX':
                            cadenaciudad = row2[0] + ' (Ciudad de México, México)'
                        elif row2[0] == 'TAM':
                            cadenaciudad = row2[0] + ' (Tampico, Tamaulipas, México)'
                        elif row2[0] == 'GDL':
                            cadenaciudad = row2[0] + ' (Guadalajara, Jalisco, México)'
                        elif row2[0] == 'CJS':
                            cadenaciudad = row2[0] + ' (Ciudad Juárez, Chihuahua, México)'
                        elif row2[0] == 'CUN':
                            cadenaciudad = row2[0] + ' (Cancún, Yucatán, México)'
                        elif row2[0] == 'TIJ':
                            cadenaciudad = row2[0] + ' (Tijuana, Baja California, México)'
                        elif row2[0] == 'HMO':
                            cadenaciudad = row2[0] + ' (Hermosillo, Sonora, México)'
                        elif row2[0] == 'CME':
                            cadenaciudad = row2[0] + ' (Ciudad del Carmen, Campeche, México)'
                        elif row2[0] == 'MID':
                            cadenaciudad = row2[0] + ' (Mérida, Yucatán, México)'
                        elif row2[0] == 'CTM':
                            cadenaciudad = row2[0] + ' (Chetumal, Quintana Roo, México)'
                        elif row2[0] == 'VER':
                            cadenaciudad = row2[0] + ' (Veracruz, Veracruz, México)'
                        elif row2[0] == 'OAX':
                            cadenaciudad = row2[0] + ' (Oaxaca de Juárez, Oaxaca, México)'
                        elif row2[0] == 'HUX':
                            cadenaciudad = row2[0] + ' (Huatulco, Oaxaca, México)'
                        elif row2[0] == 'ZIH':
                            cadenaciudad = row2[0] + ' (Zihuatanejo, Guerrero, México)'
                        elif row2[0] == 'PVR':
                            cadenaciudad = row2[0] + ' (Puerto Vallarta, Jalisco, México)'
                        elif row2[0] == 'LIM':
                            cadenaciudad = row2[0] + ' (Lima, Perú)'
                        elif row2[0] == 'HAV':
                            cadenaciudad = row2[0] + ' (La Habana, Cuba)'
                        elif row2[0] == 'BOG':
                            cadenaciudad = row2[0] + ' (Bogotá, Colombia)'
                        elif row2[0] == 'MIA':
                            cadenaciudad = row2[0] + ' (Miami, Florida, Estados Unidos)'
                        elif row2[0] == 'LAX':
                            cadenaciudad = row2[0] + ' (Los Angeles, California, Estados Unidos)'
                        elif row2[0] == 'JFK':
                            cadenaciudad = row2[0] + ' (New York, Estados Unidos)'
                        elif row2[0] == 'TRC':
                            cadenaciudad = row2[0] + ' (Torreón, Coahuila, México)'
                        elif row2[0] == 'PXM':
                            cadenaciudad = row2[0] + ' (Puerto Escondido, Oaxaca, México)'
                        elif row2[0] == 'ACA':
                            cadenaciudad = row2[0] + ' (Acapulco, Guerrero, México)'
                        elif row2[0] == 'MZT':
                            cadenaciudad = row2[0] + ' (Mazatlán, Sinaloa, México)'
                        elif row2[0] == 'GUA':
                            cadenaciudad = row2[0] + ' (Ciudad de Guatemala, Guatemala)'
                        elif row2[0] == 'AGU':
                            cadenaciudad = row2[0] + ' (Aguascalientes, México)'
                        elif row2[0] == 'VSA':
                            cadenaciudad = row2[0] + ' (Villahermosa, Tabasco, México)'
                        elif row2[0] == 'BZE':
                            cadenaciudad = row2[0] + ' (Ladyville, Belice)'
                        elif row2[0] == 'DFW':
                            cadenaciudad = row2[0] + ' (Texas, Estados Unidos)'
                        elif row2[0] == 'CZM':
                            cadenaciudad = row2[0] + ' (Cozumel, Quintana Roo, México)'
                        elif row2[0] == 'ORD':
                            cadenaciudad = row2[0] + ' (Illinois, Estados Unidos)'
                        elif row2[0] == 'PHX':
                            cadenaciudad = row2[0] + ' (Phoenix, Arizona, Estados Unidos)'
                        elif row2[0] == 'CUU':
                            cadenaciudad = row2[0] + ' (Chihuahua, Chihuahua)'
                        elif row2[0] == 'QRO':
                            cadenaciudad = row2[0] + ' (Querétaro, México)'
                        elif row2[0] == 'BJX':
                            cadenaciudad = row2[0] + ' (Guanajuato, México)'
                        elif row2[0] == 'PBC':
                            cadenaciudad = row2[0] + ' (Puebla, México)'
                        elif row2[0] == 'PHL':
                            cadenaciudad = row2[0] + ' (Filadelfia/Tinicum Township, Pensilvania, Estados Unidos)'
                        elif row2[0] == 'SLP':
                            cadenaciudad = row2[0] + ' (San Luis Potosí, México)'
                        elif row2[0] == 'CLT':
                            cadenaciudad = row2[0] + ' (Charlotte, Carolina del Norte, Estados Unidos)'
                        elif row2[0] == 'YYZ':
                            cadenaciudad = row2[0] + ' (Ontario, Canadá)'
                        elif row2[0] == 'IAH':
                            cadenaciudad = row2[0] + ' (Houston, Texas, Estados Unidos)'
                        elif row2[0] == 'YVR':
                            cadenaciudad = row2[0] + ' (Richmond, Canadá)'
                        elif row2[0] == 'CDG':
                            cadenaciudad = row2[0] + ' (París, Francia)'
                        elif row2[0] == 'ZCL':
                            cadenaciudad = row2[0] + ' (Zacatecas, Zacatecas, México)'
                        elif row2[0] == 'AMS':
                            cadenaciudad = row2[0] + ' (Ámsterdam, Países Bajos)'
                        elif row2[0] == 'ATL':
                            cadenaciudad = row2[0] + ' (Atlanta, Estados Unidos)'
                        elif row2[0] == 'CEN':
                            cadenaciudad = row2[0] + ' (Ciudad Obregón, Sonora, México)'
                        elif row2[0] == 'MAD':
                            cadenaciudad = row2[0] + ' (Madrid, España)'
                        elif row2[0] == 'SCL':
                            cadenaciudad = row2[0] + ' (Santiago, Chile)'


                        #Primer arreglo para los nombres.
                        ciudades["nombres"].append(cadenaciudad)

                        #Segundo arreglo para objetos de tipo Ciudad.
                        ciudades["coordenadas"].append(Ciudad.Ciudad(row2[0], row2[2], row2[3]))

                    #Elimina al nombre del conjunto para evitar introducir nuevamente
                    #la misma ciudad en el diccionario.
                    conjunto.discard(row2[0])

                #Revisa para la segunda ciudad que aparece en la fila correspondiente en el .csv.
                if row2[1] in conjunto:
                    if row2[1] == 'TLC':
                        cadenaciudad = row2[1] + ' (Toluca, Estado de México, México)'
                    elif row2[1] == 'MTY':
                        cadenaciudad = row2[1] + ' (Monterrey, Nuevo León, México)'
                    elif row2[1] == 'MEX':
                        cadenaciudad = row2[1] + ' (Ciudad de México, México)'
                    elif row2[1] == 'TAM':
                        cadenaciudad = row2[1] + ' (Tampico, Tamaulipas, México)'
                    elif row2[1] == 'GDL':
                        cadenaciudad = row2[1] + ' (Guadalajara, Jalisco, México)'
                    elif row2[1] == 'CJS':
                        cadenaciudad = row2[1] + ' (Ciudad Juárez, Chihuahua, México)'
                    elif row2[1] == 'CUN':
                        cadenaciudad = row2[1] + ' (Cancún, Yucatán, México)'
                    elif row2[1] == 'TIJ':
                        cadenaciudad = row2[1] + ' (Tijuana, Baja California, México)'
                    elif row2[1] == 'HMO':
                        cadenaciudad = row2[1] + ' (Hermosillo, Sonora, México)'
                    elif row2[1] == 'CME':
                        cadenaciudad = row2[1] + ' (Ciudad del Carmen, Campeche, México)'
                    elif row2[1] == 'MID':
                        cadenaciudad = row2[1] + ' (Mérida, Yucatán, México)'
                    elif row2[1] == 'CTM':
                        cadenaciudad = row2[1] + ' (Chetumal, Quintana Roo, México)'
                    elif row2[1] == 'VER':
                        cadenaciudad = row2[1] + ' (Veracruz, Veracruz, México)'
                    elif row2[1] == 'OAX':
                        cadenaciudad = row2[1] + ' (Oaxaca de Juárez, Oaxaca, México)'
                    elif row2[1] == 'HUX':
                        cadenaciudad = row2[1] + ' (Huatulco, Oaxaca, México)'
                    elif row2[1] == 'ZIH':
                        cadenaciudad = row2[1] + ' (Zihuatanejo, Guerrero, México)'
                    elif row2[1] == 'PVR':
                        cadenaciudad = row2[1] + ' (Puerto Vallarta, Jalisco, México)'
                    elif row2[1] == 'LIM':
                        cadenaciudad = row2[1] + ' (Lima, Perú)'
                    elif row2[1] == 'HAV':
                        cadenaciudad = row2[1] + ' (La Habana, Cuba)'
                    elif row2[1] == 'BOG':
                        cadenaciudad = row2[1] + ' (Bogotá, Colombia)'
                    elif row2[1] == 'MIA':
                        cadenaciudad = row2[1] + ' (Miami, Florida, Estados Unidos)'
                    elif row2[1] == 'LAX':
                        cadenaciudad = row2[1] + ' (Los Angeles, California, Estados Unidos)'
                    elif row2[1] == 'JFK':
                        cadenaciudad = row2[1] + ' (New York, Estados Unidos)'
                    elif row2[1] == 'TRC':
                        cadenaciudad = row2[1] + ' (Torreón, Coahuila, México)'
                    elif row2[1] == 'PXM':
                        cadenaciudad = row2[1] + ' (Puerto Escondido, Oaxaca, México)'
                    elif row2[1] == 'ACA':
                        cadenaciudad = row2[1] + ' (Acapulco, Guerrero, México)'
                    elif row2[1] == 'MZT':
                        cadenaciudad = row2[1] + ' (Mazatlán, Sinaloa, México)'
                    elif row2[1] == 'GUA':
                        cadenaciudad = row2[1] + ' (Ciudad de Guatemala, Guatemala)'
                    elif row2[1] == 'AGU':
                        cadenaciudad = row2[1] + ' (Aguascalientes, México)'
                    elif row2[1] == 'VSA':
                        cadenaciudad = row2[1] + ' (Villahermosa, Tabasco, México)'
                    elif row2[1] == 'BZE':
                        cadenaciudad = row2[1] + ' (Ladyville, Belice)'
                    elif row2[1] == 'DFW':
                        cadenaciudad = row2[1] + ' (Texas, Estados Unidos)'
                    elif row2[1] == 'CZM':
                        cadenaciudad = row2[1] + ' (Cozumel, Quintana Roo, México)'
                    elif row2[1] == 'ORD':
                        cadenaciudad = row2[1] + ' (Illinois, Estados Unidos)'
                    elif row2[1] == 'PHX':
                        cadenaciudad = row2[1] + ' (Phoenix, Arizona, Estados Unidos)'
                    elif row2[1] == 'CUU':
                        cadenaciudad = row2[1] + ' (Chihuahua, Chihuahua)'
                    elif row2[1] == 'QRO':
                        cadenaciudad = row2[1] + ' (Querétaro, México)'
                    elif row2[1] == 'BJX':
                        cadenaciudad = row2[1] + ' (Guanajuato, México)'
                    elif row2[1] == 'PBC':
                        cadenaciudad = row2[1] + ' (Puebla, México)'
                    elif row2[1] == 'PHL':
                        cadenaciudad = row2[1] + ' (Filadelfia/Tinicum Township, Pensilvania, Estados Unidos)'
                    elif row2[1] == 'SLP':
                        cadenaciudad = row2[1] + ' (San Luis Potosí, México)'
                    elif row2[1] == 'CLT':
                        cadenaciudad = row2[1] + ' (Charlotte, Carolina del Norte, Estados Unidos)'
                    elif row2[1] == 'YYZ':
                        cadenaciudad = row2[1] + ' (Ontario, Canadá)'
                    elif row2[1] == 'IAH':
                        cadenaciudad = row2[1] + ' (Houston, Texas, Estados Unidos)'
                    elif row2[1] == 'YVR':
                        cadenaciudad = row2[1] + ' (Richmond, Canadá)'
                    elif row2[1] == 'CDG':
                        cadenaciudad = row2[1] + ' (París, Francia)'
                    elif row2[1] == 'ZCL':
                        cadenaciudad = row2[1] + ' (Zacatecas, Zacatecas, México)'
                    elif row2[1] == 'AMS':
                        cadenaciudad = row2[1] + ' (Ámsterdam, Países Bajos)'
                    elif row2[1] == 'ATL':
                        cadenaciudad = row2[1] + ' (Atlanta, Estados Unidos)'
                    elif row2[1] == 'CEN':
                        cadenaciudad = row2[1] + ' (Ciudad Obregón, Sonora, México)'
                    elif row2[1] == 'MAD':
                        cadenaciudad = row2[1] + ' (Madrid, España)'
                    elif row2[1] == 'SCL':
                        cadenaciudad = row2[1] + ' (Santiago, Chile)'

                    #Primer arreglo para los nombres.
                    ciudades["nombres"].append(cadenaciudad)

                    #Segundo arreglo para objetos de tipo Ciudad.
                    ciudades["coordenadas"].append(Ciudad.Ciudad(row2[1], row2[4], row2[5]))

                    #Elimina al nombre del conjunto para evitar introducir nuevamente
                    #la misma ciudad en el diccionario.
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
            Función que se encarga de realizar la búsqueda en el arreglo de objetos de tipo Ciudad
            con base en el nombre pasado como parámetro.
        """
        for i in range(1, len(self.arregloCiudades())):
            if ciudad == self.arregloNombres()[i]:
                return self.arregloCiudades()[i]
