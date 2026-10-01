# Práctica 2: Herramientas (Tools) y Function Calling

En esta práctica, aprenderemos sobre el concepto de **Function Calling** (Llamada a Funciones) y cómo el Google ADK nos permite dotar a nuestros agentes de habilidades adicionales.

## ¿Qué es el Function Calling?
Los Modelos de Lenguaje Grandes (LLMs) como Gemini son expertos en texto, pero por defecto no pueden interactuar con el mundo exterior (por ejemplo, buscar en internet, leer una base de datos o consultar una API del clima). 

El "Function Calling" soluciona esto. Permite que el modelo, en lugar de responder directamente con texto, solicite ejecutar una función específica si determina que es necesario para responder a la petición del usuario. 

Con Google ADK, convertir una función de Python en una herramienta para el agente es extremadamente sencillo:
1. Defines una función normal de Python.
2. Agregas **Type Hints** (indicaciones de tipo, como `str`, `int`) a los parámetros.
3. Escribes un **Docstring** (comentario de documentación) claro que explique qué hace la función y qué significan sus parámetros.
El ADK lee automáticamente esta información y le explica al modelo de Gemini cómo y cuándo usar la herramienta.

## Estructura del Directorio
Esta práctica sigue las mejores convenciones para estructurar un agente complejo:
- `agents/`: Contiene sub-agentes si nuestro agente principal necesitara delegar tareas (en esta práctica estará vacío).
- `prompts/`: Carpeta dedicada a almacenar los mensajes y personalidades del agente, separando la lógica del texto.
- `tools/`: Aquí viven nuestras funciones de Python que el agente usará como herramientas.
- `knowledge/`: Para almacenar datos y documentos base de conocimiento (vacío por ahora).
- `agent.py`: Archivo principal donde unimos el prompt, las herramientas y definimos nuestro agente.
- `__init__.py`: Expone nuestro agente hacia afuera.
- `tests/`: Pruebas unitarias para asegurar que nuestro código funciona.
