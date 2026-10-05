"""DefiniciÃ³n del agente de voz."""

from google.adk.agents import Agent
from .prompts.instrucciones import PROMPT_VOZ

# CRÃTICO: Para la Live API (agentes de voz), debemos usar un modelo que termine en "-live"
# Esto permite el procesamiento nativo de audio a audio sin necesidad de STT/TTS.
root_agent = Agent(
    name="agente_voz",
    instruction=PROMPT_VOZ,
    model="gemini-3.8-live"
)
