# 🎲 Proyecto Juegos de Azar

Una librería Python que implementa simuladores simples de juegos de azar: lanzamiento de dados y extracción de cartas. Desarrollado como proyecto de prácticas, siguiendo buenas prácticas de programación y uso de control de versiones con Git.

---

## 🚀 Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/SebastianGH20/proyecto_juegos_azar.git
   cd proyecto_juegos_azar
   ```

2. Crea un entorno virtual (recomendado):
   ```bash
   python -m venv juegos_azar_env
   juegos_azar_env\Scripts\activate   # En Windows
   ```

3. Instala el paquete en modo desarrollo:
   ```bash
   pip install -e .
   ```

---

## 📁 Estructura del Proyecto

```
proyecto_juegos_azar/
├── juegos_azar/              # Código fuente (librería)
│   ├── __init__.py
│   ├── cartas.py
│   └── dados.py
├── scripts/                  # Script ejecutable principal
│   └── main.py
├── test/                     # (Opcional) Pruebas unitarias
├── config/                   # Configuración (no usada en este ejemplo)
├── data/                     # Datos (no usada en este ejemplo)
├── README.md
├── setup.py
└── .gitignore
```

---

## 🧠 Uso de la Librería

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

## ▶️ Ejecutar el Script Principal

Desde la raíz del proyecto, ejecuta:

```bash
python scripts/main.py
```

Esto demostrará el funcionamiento tanto del simulador de cartas como del de dados.

---

## ✅ Buenas Prácticas Aplicadas

- ✅ Programación orientada a objetos
- ✅ Modularidad del código
- ✅ Control de versiones con Git y ramas por funcionalidad
- ✅ Instalación como paquete (`pip install -e .`)
- ✅ Código limpio y reutilizable

---

## 📝 Licencia

Este proyecto está licenciado bajo la Licencia MIT.

---

## 👤 Autor

**Sebastián González**  
📧 sebastian.gonzalez.hincapie@gmail.com  
🔗 [GitHub](https://github.com/SebastianGH20)
