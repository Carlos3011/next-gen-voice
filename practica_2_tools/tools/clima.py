# AquÃ­ definimos nuestra herramienta (Tool)
# Observa cÃ³mo usamos type hints (ciudad: str, -> str) y el docstring.
# El modelo Gemini leerÃ¡ el docstring para entender QUÃ‰ hace la funciÃ³n y CÃ“MO llamarla.

def obtener_clima(ciudad: str) -> str:
    """
    Obtiene el clima actual para una ciudad especificada.
    Usa esta herramienta cuando el usuario pregunte por el clima de un lugar.
    
    Args:
        ciudad (str): El nombre de la ciudad para la cual consultar el clima (ej. 'Madrid', 'BogotÃ¡').
        
    Returns:
        str: Una descripciÃ³n simulada del clima en esa ciudad.
    """
    # En un caso real, aquÃ­ harÃ­amos una peticiÃ³n HTTP (request) a una API de clima (como OpenWeather).
    # Para fines de esta prÃ¡ctica, simularemos la respuesta.
    
    ciudad_limpia = ciudad.strip().lower()
    
    if ciudad_limpia == "madrid":
        return f"El clima en {ciudad} es soleado, con 25Â°C."
    elif ciudad_limpia == "bogotÃ¡" or ciudad_limpia == "bogota":
        return f"El clima en {ciudad} es lluvioso, con 15Â°C."
    else:
        return f"El clima en {ciudad} es templado, con 20Â°C y parcialmente nublado."
