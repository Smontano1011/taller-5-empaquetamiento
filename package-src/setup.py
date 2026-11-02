
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from setuptools import find_packages, setup

# Metadatos del paquete
NAME = "model-abandono"
DESCRIPTION = "Ejemplo de empaquetamiento de modelo de bank churn."
URL = ""
EMAIL = "jf.perez33@uniandes.edu.co"
AUTHOR = "juanfperez"
REQUIRES_PYTHON = ">=3.12.0"
long_description = DESCRIPTION

about = {}
ROOT_DIR = Path(__file__).resolve().parent
REQUIREMENTS_DIR = ROOT_DIR / "requirements"
PACKAGE_DIR = ROOT_DIR / "model"

# Obtener la versión del paquete
with open(PACKAGE_DIR / "VERSION", encoding="utf-8") as f:
    _version = f.read().strip()
    about["__version__"] = _version


# Lista de dependencias del paquete
def list_reqs(fname="requirements.txt"):
    with open(REQUIREMENTS_DIR / fname, encoding="utf-8") as fd:
        return fd.read().splitlines()


# Configuración del empaquetamiento
setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,

    # Incluir los módulos Python
    packages=find_packages(exclude=("tests",)),

    # Incluir archivos necesarios para ejecutar el modelo
    package_data={
        "model": [
            "VERSION",
            "config.yml",
            "trained/*.pkl",
        ]
    },

    # Dependencias
    install_requires=list_reqs(),
    extras_require={},

    # Incluir archivos adicionales definidos en MANIFEST.in
    include_package_data=True,

    license="BSD-3",
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
)
