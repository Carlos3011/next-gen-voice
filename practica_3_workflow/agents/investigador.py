"""
Agente encargado de la investigaciÃ³n de la informaciÃ³n.
"""
from google.adk.agents import Agent
from practica_3_workflow.prompts.instrucciones import PROMPT_INVESTIGADOR

# Creamos el agente investigador.
# Al establecer output_key="datos_investigados", este agente guardarÃ¡ automÃ¡ticamente
# su respuesta final en el estado compartido de la sesiÃ³n bajo esa clave.
investigador = Agent(
    name="Investigador",
    instruction=PROMPT_INVESTIGADOR,
    output_key="datos_investigados"
)
