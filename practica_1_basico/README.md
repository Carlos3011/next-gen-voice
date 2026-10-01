# Práctica 1: Estructura Básica de un Agente

¡Bienvenido a la primera práctica! Aquí aprenderemos cómo se organiza un proyecto de agentes en producción. Una buena organización es clave para mantener nuestro código limpio y escalable.

## Estructura de Carpetas

En este directorio encontrarás las siguientes carpetas. Cada una tiene un propósito específico:

- **`agents/`**: ¿Para qué sirve? Si nuestro agente es complejo y necesita delegar tareas, aquí definimos sub-agentes especialistas (por ejemplo, un agente solo para buscar en internet). Por ahora está vacía, ¡pero es bueno tenerla lista!
- **`prompts/`**: ¿Para qué sirve? Aquí guardamos las "instrucciones" (system prompts) y plantillas que le dicen a nuestro agente cómo debe comportarse, qué personalidad debe tener y qué reglas debe seguir.
- **`tools/`**: ¿Para qué sirve? Los agentes pueden usar "herramientas" (funciones Python) para interactuar con el mundo real (como buscar en Google, leer un archivo, o consultar una API). Aquí guardamos esas funciones.
- **`knowledge/`**: ¿Para qué sirve? Aquí pondremos documentos, PDFs o archivos de texto que el agente podrá leer para aprender información nueva que no conoce (esto se llama RAG - Retrieval Augmented Generation).

## ¿Por qué usamos esta estructura?

Separar nuestro código de esta manera nos permite:
1. **Mantener el orden:** Es más fácil encontrar dónde cambiar una instrucción o dónde agregar una herramienta.
2. **Escalar:** Si el proyecto crece, no tendremos todo mezclado en un solo archivo gigante.
3. **Reutilizar:** Podemos usar las mismas herramientas o bases de conocimiento en diferentes agentes.
