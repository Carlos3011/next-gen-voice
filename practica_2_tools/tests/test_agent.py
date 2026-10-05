import pytest
from practica_2_tools.agent import root_agent
from practica_2_tools.tools.clima import obtener_clima

def test_agente_tiene_herramientas():
    # Comprobamos que el agente tiene exactamente 1 herramienta configurada
    assert len(root_agent.tools) == 1
    
    # Comprobamos que la herramienta es la función obtener_clima
    assert root_agent.tools[0] == obtener_clima

def test_funcion_obtener_clima():
    # Probamos la lógica interna de nuestra herramienta de Python
    resultado_puebla = obtener_clima("Puebla")
    assert "soleado" in resultado_puebla
    assert "22" in resultado_puebla
    
    resultado_cdmx = obtener_clima("CDMX")
    assert "lluvia" in resultado_cdmx
    
    resultado_otro = obtener_clima("Tokyo")
    assert "templado" in resultado_otro
