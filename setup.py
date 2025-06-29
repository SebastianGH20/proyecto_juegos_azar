from setuptools import setup, find_packages

setup(
    name="Proyecto_Juegos_Azar",
    version="0.1.0",
    packages=find_packages(),  # Busca en el directorio raíz
    install_requires=[],
    author="Sebastián González",
    author_email="sebastian.gonzalez.hincapie@gmail.com",
    description="Simuladores de juegos de azar: dados y cartas",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SebastianGH20/proyecto_juegos_azar",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Games/Entertainment :: Simulation",
    ],
    python_requires=">=3.6",
)
