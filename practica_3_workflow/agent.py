"""
OrquestaciÃ³n del workflow utilizando SequentialAgent.
"""
from google.adk.agents import SequentialAgent
from practica_3_workflow.agents.investigador import investigador
from practica_3_workflow.agents.redactor import redactor

# SequentialAgent ejecuta los agentes en el orden exacto en el que se proporcionan.
# El flujo de ejecuciÃ³n serÃ¡: 
# 1. Investigador procesa el input del usuario y guarda en 'datos_investigados'.
# 2. Redactor toma 'datos_investigados' y genera el artÃ­culo final.
root_agent = SequentialAgent(
    name="OrquestadorDeContenido",
    sub_agents=[investigador, redactor]
)
