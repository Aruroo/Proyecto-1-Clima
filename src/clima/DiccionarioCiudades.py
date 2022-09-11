import csv
import Ciudad

class DiccionarioCiudades():

    def __init__(self, ciudades):
        for llave in ciudades:
            setattr(self, llave, ciudades[llave])


if __name__ == "__main__":
    ciudades = {
        "nombres": [],
        "coordenadas": []
    }
    resultado = DiccionarioCiudades(ciudades)


    tamaño = 4

    with open('ciudades.csv') as f:
        reader = csv.reader(f)
        for row1 in reader:
            #Datos de la ciudad 1.
            nombre1 = row1[0]
            ciudad1 = Ciudad.Ciudad(row1[2],row1[4])

            #Primera lista para los nombres.
            ciudades["nombres"].append(nombre1)

            #Segunda lista para las coordenadas.
            ciudades["coordenadas"].append(ciudad1)

            for row2 in reader:
                #Datos de la ciudad 2.
                nombre2 = row2[1]

                if row1 != row2:
                    ciudad2 = Ciudad.Ciudad(row1[2],row1[4])
                    latitud2 = row2[3]
                    altitud2 = row2[5]

                    #Primera lista para los nombres.
                    ciudades["nombres"].append(nombre2)

                    #Segunda lista para las coordenadas.
                    ciudades["coordenadas"].append(ciudad2)
