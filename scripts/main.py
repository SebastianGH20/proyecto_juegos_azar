# scripts/main.py

from juegos_azar.cartas import SimuladorCartas
from juegos_azar.dados import SimuladorDados

def ejecutar_simulador_cartas():
    print("🎴 Simulador de Cartas")
    baraja = SimuladorCartas()
    carta = baraja.sacar_carta()
    if carta:
        print(f"Carta sacada: {carta}")
    print(f"Cartas restantes en la baraja: {len(baraja.cartas)}")
    print("-" * 40)

def ejecutar_simulador_dados():
    print("🎲 Simulador de Dados")
    dado = SimuladorDados(caras=6)
    resultados = dado.tirar(5)
    print(f"Resultado de 5 tiradas de un dado de 6 caras: {resultados}")
    print("-" * 40)

if __name__ == "__main__":
    ejecutar_simulador_cartas()
    ejecutar_simulador_dados()
