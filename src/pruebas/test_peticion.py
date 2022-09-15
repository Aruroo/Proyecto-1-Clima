import unittest
import os
from clima import Peticion
class TestPeticion(unittest.TestCase):

    def test_peticion_correcta(self):
        """
        Prueba que se creen archivos JSON de forma satisfactoria
        dada una entrada con datos correctos.
        """
        peticionCorrecta = Peticion(19.3242765,-99.1813205,"Ciencias")
        ruta = "../caché/peticiones/Ciencias"+".json"
        self.assertTrue(os.path.isfile(ruta))

    def test_peticion_incorrecta(self):
        """
        Prueba que se haga la petición, aún teniendo coordenadas incorrectas
        """
        peticionCorrecta = Peticion(19.3242765,1,"Ciencias")
        ruta = "../caché/peticiones/Ciencias"+".json"
        self.assertTrue(os.path.isfile(ruta))   

    def test_necesita_actualizase(self):
       """
       Prueba que el método necesitaActualizarse(self, dict)
       funcione correctamente.
       
       (Devuelve true si han pasado más de 5 minutos desde la última petición,
       recibiendo un diccionario de tiempos.)
       
       """
       diccionarioTiempos ={}
       diccionarioTiempos["ano"] = 2022
       diccionarioTiempos["mes"] = 9                 
       diccionarioTiempos["dia"] =15
       diccionarioTiempos["hora"] =14
       diccionarioTiempos["minuto"] =1
       bol = Peticion.__necesitaActualizarse(diccionarioTiempos)
       self.assertTrue(bol)

