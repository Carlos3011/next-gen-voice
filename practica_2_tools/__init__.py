# Este archivo expone el agente principal para que otros paquetes puedan importarlo fÃ¡cilmente
# Por ejemplo, podrÃ­amos hacer: from practica_2_tools import root_agent

from .agent import root_agent

__all__ = ["root_agent"]
