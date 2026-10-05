# Importamos la clase base Agent del kit de desarrollo de Google (ADK)
from google.adk.agents import Agent

# Importamos nuestro texto de instrucciones
from .prompts.instrucciones import PROMPT_ASISTENTE

# AquÃ­ instanciamos nuestro agente principal.
# Le damos un nombre, elegimos el modelo de lenguaje e insertamos las instrucciones.
root_agent = Agent(
    name="asistente_amable",
    model="gemini-3.8-flash",
    instruction=PROMPT_ASISTENTE
)
