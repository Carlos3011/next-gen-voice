"""
Pruebas unitarias para verificar la estructura del workflow multi-agente.
"""
from google.adk.agents import SequentialAgent
from practica_3_workflow.agent import root_agent

def test_workflow_structure():
    # 1. Verificar que root_agent es un SequentialAgent (orquestador)
    assert isinstance(root_agent, SequentialAgent), "root_agent debe ser una instancia de SequentialAgent"

    # 2. Verificar que contiene exactamente 2 sub-agentes
    assert len(root_agent.sub_agents) == 2, "El workflow debe tener exactamente 2 agentes"

    # 3. Verificar el orden y los nombres de los agentes
    assert root_agent.sub_agents[0].name == "Investigador", "El primer agente debe llamarse 'Investigador'"
    assert root_agent.sub_agents[1].name == "Redactor", "El segundo agente debe llamarse 'Redactor'"

    # 4. Verificar la configuraciÃ³n del estado de sesiÃ³n compartido
    assert root_agent.sub_agents[0].output_key == "datos_investigados", "El investigador debe exportar su salida a 'datos_investigados'"
