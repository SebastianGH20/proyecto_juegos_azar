# juegos_azar/dados.py

import random

class SimuladorDados:
    def __init__(self, caras=6):
        self.caras = caras

    def tirar(self, veces=1):
        resultados = []
        for _ in range(veces):
            resultado = random.randint(1, self.caras)
            resultados.append(resultado)
        return resultados
