# Aquí definimos nuestra herramienta (Tool)
# Observa cómo usamos type hints (ciudad: str, -> str) y el docstring.
# El modelo Gemini leerá el docstring para entender QUÉ hace la función y CÓMO llamarla.

def obtener_clima(ciudad: str) -> str:
    """
    Obtiene el clima actual para una ciudad especificada.
    Usa esta herramienta cuando el usuario pregunte por el clima de un lugar.
    
    Args:
        ciudad (str): El nombre de la ciudad para la cual consultar el clima (ej. 'Madrid', 'Bogotá').
        
    Returns:
        str: Una descripción simulada del clima en esa ciudad.
    """
    # En un caso real, aquí haríamos una petición HTTP (request) a una API de clima (como OpenWeather).
    # Para fines de esta práctica, simularemos la respuesta.
    
    ciudad_limpia = ciudad.strip().lower()
    
    if ciudad_limpia == "madrid":
        return f"El clima en {ciudad} es soleado, con 25°C."
    elif ciudad_limpia == "bogotá" or ciudad_limpia == "bogota":
        return f"El clima en {ciudad} es lluvioso, con 15°C."
    else:
        return f"El clima en {ciudad} es templado, con 20°C y parcialmente nublado."
