import unittest
from juegos_azar.cartas import SimuladorCartas

class TestSimuladorCartas(unittest.TestCase):

    def test_sacar_carta_disminuye_mazo(self):
        baraja = SimuladorCartas()
        cartas_antes = len(baraja.cartas)
        baraja.sacar_carta()
        cartas_despues = len(baraja.cartas)
        self.assertEqual(cartas_antes - 1, cartas_despues)

    def test_reiniciar_baraja(self):
        baraja = SimuladorCartas()
        baraja.sacar_carta()
        baraja.reiniciar_baraja()
        self.assertEqual(len(baraja.cartas), 52)

if __name__ == '__main__':
    unittest.main()
