import sys
import os
import pytest

# Aseguramos que Python pueda encontrar el directorio principal del paquete
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importamos el agente que queremos probar
from practica_1_basico.agent import root_agent

def test_root_agent_configuracion():
    """
    Prueba unitaria didÃ¡ctica para verificar que nuestro agente estÃ¡
    configurado correctamente antes de usarlo.
    """
    # 1. Comprobamos que el nombre es correcto
    assert root_agent.name == "asistente_amable", "El nombre del agente deberÃ­a ser 'asistente_amable'"
    
    # 2. Comprobamos que usa el modelo correcto (gemini-3.8-flash es rÃ¡pido y eficiente)
    assert root_agent.model == "gemini-3.8-flash", "El modelo configurado no es el esperado"
    
    # 3. Comprobamos que, al ser bÃ¡sico, no tiene herramientas (tools)
    # Puede ser None o una lista vacÃ­a
    assert not root_agent.tools, "El agente de la prÃ¡ctica bÃ¡sica no deberÃ­a tener herramientas"
