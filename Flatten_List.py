def aplanar_lista(lista):
    # Caso Base: Lista vacía retorna una lista vacía
    if not lista:
        return []
        
    cabeza = lista[0]
    resto = lista[1:]
    
    # Paso Recursivo A: Si la cabeza es otra lista, la aplanamos recursivamente
    if isinstance(cabeza, list):
        return aplanar_lista(cabeza) + aplanar_lista(resto)
        
    # Paso Recursivo B: Si es un número/elemento plano, lo conservamos
    return [cabeza] + aplanar_lista(resto)

# === PRUEBAS DE EJECUCIÓN ===
if __name__ == "__main__":
    print("--- 5. Flatten List ---")
    lista_anidada_1 = [1, [2, [3, 4], 5]]
    lista_anidada_2 = [[1, 2, 3], [4, 5], 6, [7, [8, 9]]]
    
    print(f"Original 1: {lista_anidada_1}")
    print(f"Aplanada 1: {aplanar_lista(lista_anidada_1)}\n")
    
    print(f"Original 2: {lista_anidada_2}")
    print(f"Aplanada 2: {aplanar_lista(lista_anidada_2)}")