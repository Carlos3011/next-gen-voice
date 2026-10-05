# Importamos la clase Agent del ADK
from google.adk.agents import Agent

# Importamos nuestro prompt y nuestra herramienta
from .prompts.instrucciones import PROMPT_TOOLS
from .tools.clima import obtener_clima

# Creamos la instancia de nuestro agente
root_agent = Agent(
    name="AgenteMeteorologico",
    model="gemini-3.8-flash", # Usamos el modelo recomendado para un buen balance de velocidad y capacidad
    instruction=PROMPT_TOOLS,
    # ¡Aquí ocurre la magia! Le pasamos la lista de funciones de Python.
    # El ADK las convertirá en herramientas comprensibles para el LLM.
    tools=[obtener_clima]
)
