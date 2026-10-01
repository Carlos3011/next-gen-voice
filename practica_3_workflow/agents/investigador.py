"""
Agente encargado de la investigación de la información.
"""
from google.adk.agents import Agent
from practica_3_workflow.prompts.instrucciones import PROMPT_INVESTIGADOR

# Creamos el agente investigador.
# Al establecer output_key="datos_investigados", este agente guardará automáticamente
# su respuesta final en el estado compartido de la sesión bajo esa clave.
investigador = Agent(
    name="Investigador",
    instruction=PROMPT_INVESTIGADOR,
    output_key="datos_investigados"
)
