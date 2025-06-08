import unittest
from juegos_azar.dados import SimuladorDados

class TestSimuladorDados(unittest.TestCase):

    def test_tirar_dado_retorna_lista(self):
        dado = SimuladorDados(caras=6)
        resultado = dado.tirar(5)
        self.assertIsInstance(resultado, list)
        self.assertEqual(len(resultado), 5)

    def test_valores_dentro_de_rango(self):
        dado = SimuladorDados(caras=10)
        resultado = dado.tirar(20)
        for valor in resultado:
            self.assertGreaterEqual(valor, 1)
            self.assertLessEqual(valor, 10)

if __name__ == '__main__':
    unittest.main()
