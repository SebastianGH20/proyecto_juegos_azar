import random

class SimuladorCartas:
    def __init__(self):
        self.cartas = self.crear_baraja()

    def crear_baraja(self):
        palos = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
        valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        baraja = []

        for palo in palos:
            for valor in valores:
                baraja.append(f"{valor} de {palo}")

        return baraja

    def sacar_carta(self):
        if not self.cartas:
            print("Ya no quedan cartas en la baraja.")
            return None
        carta = random.choice(self.cartas)
        self.cartas.remove(carta)
        return carta

    def reiniciar_baraja(self):
        self.cartas = self.crear_baraja()
