import main

import unittest

class TestTrashCity(unittest.TestCase):

    def setUp(self):
        self.trash_city = main.TrashCity()

    def test_agregarCamiones(self):
        camion1 = main.Camion(1)
        camion2 = main.Camion(2)

        self.trash_city.agregarCamiones(camion1)
        self.assertEqual(len(self.trash_city.Camiones), 1)

        self.trash_city.agregarCamiones(camion1)
        self.assertEqual(len(self.trash_city.Camiones), 1)

        self.trash_city.agregarCamiones(camion2)
        self.assertEqual(len(self.trash_city.Camiones), 2)

    def test_agregarConductores(self):
        conductor1 = main.Personal("Juan", 1)
        conductor2 = main.Personal("Pedro", 2)

        self.trash_city.agregarConductores(conductor1)
        self.assertEqual(len(self.trash_city.Conductores), 1)

        self.trash_city.agregarConductores(conductor1)
        self.assertEqual(len(self.trash_city.Conductores), 1)

        self.trash_city.agregarConductores(conductor2)
        self.assertEqual(len(self.trash_city.Conductores), 2)

    def test_agregarAsistentes(self):
        asistente1 = main.Personal("Ana", 1)
        asistente2 = main.Personal("Maria", 2)

        self.trash_city.agregarAsistentes(asistente1)
        self.assertEqual(len(self.trash_city.Asistentes), 1)

        self.trash_city.agregarAsistentes(asistente1)
        self.assertEqual(len(self.trash_city.Asistentes), 1)

        self.trash_city.agregarAsistentes(asistente2)
        self.assertEqual(len(self.trash_city.Asistentes), 2)

    def test_calcularVidrio(self):
        turno = main.Turno(1, 1, 1, 1)

        total_vidrio = self.trash_city.calcularVidrio(turno, 100)
        self.assertEqual(total_vidrio, 100)

        total_vidrio = self.trash_city.calcularVidrio(turno, 50)
        self.assertEqual(total_vidrio, 150)

        total_vidrio = self.trash_city.calcularVidrio(turno, 75)
        self.assertEqual(total_vidrio, 225)

if __name__ == '__main__':
    unittest.main()
