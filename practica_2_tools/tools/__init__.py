# Directorio Tools (Herramientas)
#
# Aquí definimos las funciones de Python que el agente usará para interactuar con su entorno.
# Recuerda que las funciones necesitan Type Hints y Docstrings claros.

from .clima import obtener_clima

__all__ = ["obtener_clima"]
