# Práctica 4: Configuración Avanzada de Agentes

Esta práctica introduce conceptos avanzados sobre cómo ajustar el comportamiento subyacente del modelo Gemini a través del ADK. 
Aprenderemos a controlar:

1. **Configuración de Generación (Tokens y Temperatura):**
   - **`temperature`**: Controla qué tan creativo o determinista es el modelo (0.0 es muy estricto/robótico, 2.0 es muy creativo/caótico).
   - **`max_output_tokens`**: Limita la longitud máxima de la respuesta que el agente puede generar (para ahorrar costos y evitar que hable de más).

2. **Configuración de Seguridad (Safety Settings):**
   - Ajusta los filtros de seguridad de Google para contenido peligroso, acoso o explícito.
   - Ideal para entender cómo proteger aplicaciones en producción.

## Archivos clave
* `agent.py`: Donde pasamos los parámetros de seguridad y generación a la instancia del `Agent`.
