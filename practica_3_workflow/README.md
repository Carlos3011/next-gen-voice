# Práctica 3: Workflow Multi-Agente

En esta práctica aprenderemos a orquestar múltiples agentes especializados utilizando `SequentialAgent`.

## Conceptos Clave

- **Orquestación Multi-Agente**: En lugar de tener un único agente para todo, dividimos el trabajo en tareas manejadas por agentes especializados (ej. Investigador y Redactor). Esto mejora el rendimiento y facilita la mantenibilidad.
- **SequentialAgent**: Es un tipo de agente que ejecuta una lista de agentes en un orden específico, pasando el control de uno a otro.
- **Carpeta `agents/`**: Se utiliza para modularizar y definir sub-agentes individuales que luego son importados y ensamblados en el agente principal.
- **Estado de Sesión Compartido**: El uso del parámetro `output_key` en un agente permite que guarde su resultado final en el estado global de la sesión bajo una clave específica (ej. `"datos_investigados"`). El siguiente agente puede acceder a estos datos usando plantillas (templating) en su prompt, como `{datos_investigados}`.
