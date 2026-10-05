import pytest
from practica_5_voz.agent import root_agent

def test_agente_usa_modelo_live():
    """Verifica que el modelo asignado al agente es compatible con la API de Live (audio)."""
    assert "live" in root_agent.model.lower(), "El agente de voz DEBE usar un modelo que termine en '-live'"

def test_agente_tiene_instrucciones():
    """Verifica que el agente tenga las instrucciones de voz configuradas correctamente."""
    assert root_agent.instruction is not None
    assert "voz" in root_agent.instruction.lower()
