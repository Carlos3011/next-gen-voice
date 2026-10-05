# Práctica 4: Agentes de Voz (Live API)

En esta práctica, aprenderemos cómo crear un agente de voz utilizando la Live API de Gemini.

## ¿Por qué usar un modelo `-live`?

A diferencia de las arquitecturas tradicionales que requieren sistemas STT (Speech-to-Text) para entender al usuario y TTS (Text-to-Speech) para hablar, la Live API procesa el audio de forma **nativa**.

Para activar esta capacidad, simplemente necesitamos usar un modelo con el sufijo `-live` (por ejemplo, `gemini-2.0-flash-live`). El modelo entiende el audio directamente y genera audio directamente, lo que resulta en una latencia mucho menor y una interacción más natural, captando el tono y la entonación sin demoras adicionales.

## Estructura
- `agent.py`: Define nuestro agente de voz.
- `prompts/instrucciones.py`: Instrucciones para que el agente mantenga respuestas cortas y conversacionales, simulando una llamada real.
