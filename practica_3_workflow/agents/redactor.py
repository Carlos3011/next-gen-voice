"""
Agente encargado de redactar el artÃ­culo final.
"""
from google.adk.agents import Agent
from practica_3_workflow.prompts.instrucciones import PROMPT_REDACTOR

# Creamos el agente redactor.
# Su prompt (PROMPT_REDACTOR) contiene el template '{datos_investigados}'.
# Antes de ejecutarse, el framework inyectarÃ¡ ahÃ­ los datos generados por el agente Investigador.
redactor = Agent(
    name="Redactor",
    instruction=PROMPT_REDACTOR
)
