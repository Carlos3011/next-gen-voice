# Aquí definimos nuestra herramienta (Tool)
# Observa cómo usamos type hints (ciudad: str, -> str) y el docstring.
# El modelo Gemini leerá el docstring para entender QUÉ hace la función y CÓMO llamarla.

def obtener_clima(ciudad: str) -> str:
    """
    Obtiene el clima actual para una ciudad especificada.
    Usa esta herramienta cuando el usuario pregunte por el clima de un lugar.
    
    Args:
        ciudad (str): El nombre de la ciudad para la cual consultar el clima (ej. 'Puebla', 'CDMX', 'Cholula').
        
    Returns:
        str: Una descripción simulada del clima en esa ciudad.
    """
    # Simulamos una respuesta de API enfocada en México/Puebla
    ciudad_limpia = ciudad.strip().lower()
    
    if ciudad_limpia == "puebla":
        return f"El clima en {ciudad} es mayormente soleado, con 22°C y excelente vista a los volcanes."
    elif ciudad_limpia == "cholula":
        return f"El clima en {ciudad} es despejado, con 24°C y viento ligero."
    elif ciudad_limpia == "atlixco":
        return f"El clima en {ciudad} es caluroso, con 28°C ideal para comer un helado o cecina."
    elif ciudad_limpia == "cdmx" or ciudad_limpia == "ciudad de mexico":
        return f"El clima en {ciudad} es nublado con probabilidad de lluvia por la tarde, 19°C."
    elif ciudad_limpia == "monterrey":
        return f"El clima en {ciudad} es extremadamente caluroso, 35°C, ponte bloqueador."
    else:
        return f"No tengo datos precisos para {ciudad}, pero asume un clima templado estándar de 20°C."
