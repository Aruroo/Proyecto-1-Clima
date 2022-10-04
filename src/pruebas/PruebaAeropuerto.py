import unittest
import csv
from Aeropuerto import Aeropuerto

class TestAeropuerto(unittest.TestCase):

    def testConstructorAeropuerto(self):
        """
            Prueba que el constructor del aeropuerto sea correcto.
        """
        aeropuerto = Aeropuerto('aeropuerto', 90.0, -10.0)
        self.assertEqual(aeropuerto.nombre, 'aeropuerto', 'Diferencia entre nombres')
        self.assertEqual(aeropuerto.latitud, 90.0, 'Diferencia entre latitudes')
        self.assertEqual(aeropuerto.altitud, -10.0, 'Diferencia entre altitudes')
