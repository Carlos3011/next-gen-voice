"""Pruebas para verificar la configuración del agente de voz."""

from ..agent import root_agent

def test_agente_usa_modelo_live():
    """
    Comprueba que el modelo asignado contiene el sufijo "-live".
    Esto es vital para que funcione el procesamiento nativo de audio.
    """
    assert "-live" in root_agent.model, (
        f"El agente de voz debe usar un modelo live. "
        f"Modelo actual: {root_agent.model}"
    )

def test_agente_tiene_instrucciones():
    """Verifica que el agente tenga las instrucciones de voz configuradas correctamente."""
    assert root_agent.instruction is not None
    assert "llamada telefónica" in root_agent.instruction.lower()
