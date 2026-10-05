import pytest
from practica_4_avanzado.agent import root_agent

def test_agente_configuracion_avanzada():
    """Verifica que el agente tenga la configuración avanzada asignada correctamente."""
    # Verificar modelo
    assert root_agent.model == "gemini-3.8-flash"
    
    # Verificar que tiene generate_content_config asignado
    assert root_agent.generate_content_config is not None
    
    # Verificar temperatura y max_output_tokens
    assert root_agent.generate_content_config.temperature == 0.1
    assert root_agent.generate_content_config.max_output_tokens == 100
    
    # Verificar filtros de seguridad
    assert len(root_agent.generate_content_config.safety_settings) == 2
