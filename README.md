# 🎰 Proyecto Juegos de Azar

Una librería Python desarrollada como proyecto de prácticas, que simula juegos de azar: 🎲 lanzamiento de dados y 🎴 extracción de cartas. Diseñado siguiendo buenas prácticas de programación, estructuras limpias y control de versiones con Git.

---

## 🚀 Instalación

1. 📥 Clona este repositorio:

```bash
git clone https://github.com/SebastianGH20/proyecto_juegos_azar.git
cd proyecto_juegos_azar
```

2. 🛠️ Crea y activa un entorno virtual (opcional pero recomendado):

```bash
python -m venv juegos_azar_env
juegos_azar_env\Scripts\activate  # En Windows
```

3. 📦 Instala el proyecto en modo desarrollo:

```bash
pip install -e .
```

---

## ▶️ Ejecución del Proyecto

4. 🔧 Desde la raíz del proyecto, ejecuta el script principal:

```bash
python scripts/main.py
```

✔️ Esto demostrará el funcionamiento del **Simulador de Cartas** y el **Simulador de Dados**.

---

5. 🧪 Ejecutar pruebas automáticas:

```bash
python -m unittest discover test
```

✔️ Resultado esperado:
```
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```

---

## 📁 Estructura del Proyecto

```
proyecto_juegos_azar/
├── juegos_azar/              # Código fuente (librería principal)
│   ├── __init__.py
│   ├── cartas.py
│   └── dados.py
├── scripts/                  # Script ejecutable
│   └── main.py
├── test/                     # Pruebas unitarias
│   ├── test_cartas.py
│   └── test_dados.py
├── config/                   # Configuración (no utilizada en este ejemplo)
├── data/                     # Datos (no utilizada en este ejemplo)
├── README.md
├── setup.py
└── .gitignore
```

---

## 🧠 Ejemplos de Uso

### 🎴 Simulador de Cartas

```python
from juegos_azar.cartas import SimuladorCartas

baraja = SimuladorCartas()
print(baraja.sacar_carta())       # Ej: "J de Picas"
print(len(baraja.cartas))         # 51
baraja.reiniciar_baraja()         # Reinicia la baraja a 52 cartas
```

---

### 🎲 Simulador de Dados

```python
from juegos_azar.dados import SimuladorDados

dado = SimuladorDados(caras=6)
print(dado.tirar(5))              # Ej: [2, 5, 1, 6, 4]
```

---

## ✅ Buenas Prácticas Aplicadas

- ✅ Programación orientada a objetos
- ✅ Modularidad del código
- ✅ Control de versiones con Git y ramas por funcionalidad
- ✅ Instalación como paquete (`pip install -e .`)
- ✅ Código limpio, documentado y reutilizable

---

## 📝 Licencia

Este proyecto está licenciado bajo la Licencia MIT.

---

## 👤 Autor

**Sebastián González**  
📧 sebastian.gonzalez.hincapie@gmail.com  
🔗 [GitHub](https://github.com/SebastianGH20)
