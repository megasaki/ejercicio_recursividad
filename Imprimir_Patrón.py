def imprimir_patron(n):
    # Caso Base: Si n es 0, detenemos la recursividad sin imprimir nada
    if n == 0:
        return
        
    # Paso Recursivo: Llamamos a la función reduciendo n ANTES de imprimir.
    imprimir_patron(n - 1)
    
    # Se ejecuta al "desenrollar" la pila de llamadas
    print("*" * n)

# === PRUEBAS DE EJECUCIÓN ===
if __name__ == "__main__":
    print("--- 3. Imprimir Patrón ---")
    print("Patrón para n = 3:")
    imprimir_patron(3)
    
    print("\nPatrón para n = 5:")
    imprimir_patron(5)