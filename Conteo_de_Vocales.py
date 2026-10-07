def contar_vocales(cadena):
    # Caso Base: Un string vacío tiene 0 vocales
    if not cadena:
        return 0
        
    # Extraemos el primer carácter y evaluamos si es vocal
    cabeza = cadena[0].lower()
    resto = cadena[1:]
    
    es_vocal = 1 if cabeza in "aeiouáéíóú" else 0
    
    # Paso Recursivo: Sumamos el resultado actual al de procesar el resto
    return es_vocal + contar_vocales(resto)

# === PRUEBAS DE EJECUCIÓN ===
if __name__ == "__main__":
    print("--- 2. Conteo de Vocales ---")
    texto_1 = "Hola Mundo desde Python"
    texto_2 = "Algoritmos recursivos"
    
    print(f"'{texto_1}' -> Tiene {contar_vocales(texto_1)} vocales.")
    print(f"'{texto_2}' -> Tiene {contar_vocales(texto_2)} vocales.")
    print(f"'' (vacío) -> Tiene {contar_vocales('')} vocales.")