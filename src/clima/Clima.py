class Clima ():

    def __init__(self):
        diccionario = DiccionarioCiudades()

    def método1():
        """
            Método que se encarga de procesar la petición o bien, arrojar datos de
            la ciudad dada por el usuario en la interfaz
        """

        """Ciudad de destino dado por el usuario (nombre): ciudaddestino"""


        """Busca en el diccionario las coordenadas"""
        coordenadasciudad = funciónAux(ciudaddestino)

        """revisar en caché"""



        """Bandera dada por la función auxiliar 2 para saber si la información
        solicitada se encuentra en caché. True si se encuentra la información en caché.
        False si no se encuentra la información en caché."""
        bandera1 = funciónAux2(ciudaddestino)

        if bandera1:

            """Devuelve el archivo .json que contiene los datos a recolectar necesarios."""

            pass
        else:

            """Realizar petición para devolver un archivo .json."""

    def funciónAux(ciudad):
        """
            Función auxiliar que se encarga de realizar la búsqueda de coordenadas
            de las ciudades pasadas como parámetro, en el diccionario
        """
        for i in range(1, diccionario.tamaño):
            if ciudad == diccionario.ciudades["nombres"][i]:
                print("Mostrando los datos de la ciudad", i)
                print("Nombre:", diccionario.ciudades["nombres"][i])
                print("Coordenadas:", diccionario.ciudades["coordenadas"][i])
                return diccionario.ciudades["coordenadas"][i]

    def funciónAux2(ciudad):
        """
            Función auxiliar que se encarga de comprobar si la información de la
            ciudad dada comp parámetro se encuentra en caché. Devuelve True si se
            encuentra en caché o False si no está en caché.
        """
        for i in range(1, diccionario.tamaño):
            if ciudad == diccionario.ciudades["nombres"][i]:
                print("Mostrando los datos de la ciudad", i)
                print("Nombre:", diccionario.ciudades["nombres"][i])
                print("Coordenadas:", diccionario.ciudades["coordenadas"][i])
                return diccionario.ciudades["coordenadas"][i]

    def método2():
        """
            Método que se encarga de recolectar los datos necesarios del archivo
            .json dado por el método anterior.
        """
