from google.adk.agents import Agent
from google.genai import types

from .prompts.instrucciones import PROMPT_AVANZADO

# Definimos la configuraciÃ³n de generaciÃ³n usando los tipos de google.genai
# AquÃ­ es donde controlamos los parÃ¡metros avanzados del modelo
config_avanzada = types.GenerateContentConfig(
    # Controla la creatividad (0.0 = robÃ³tico/estricto, 2.0 = muy creativo/alucinaciÃ³n)
    temperature=0.1,
    
    # Limita la cantidad de texto que puede devolver (para ahorrar costos)
    max_output_tokens=100,
    
    # Configuraciones de seguridad para bloquear contenido indeseado
    safety_settings=[
        types.SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
            threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        ),
        types.SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
            threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        )
    ]
)

root_agent = Agent(
    name="agente_seguro_avanzado",
    model="gemini-3.8-flash",
    instruction=PROMPT_AVANZADO,
    generate_content_config=config_avanzada
)
