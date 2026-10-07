def multiplicar(a, b):
    # Caso Base: Cualquier número multiplicado por 0 es 0
    if b == 0:
        return 0
    
    # Manejo de números negativos para 'b'
    if b < 0:
        return -multiplicar(a, -b)
        
    # Paso Recursivo: Sumar 'a' a la multiplicación de 'a' por (b-1)
    return a + multiplicar(a, b - 1)

# === PRUEBAS DE EJECUCIÓN ===
if __name__ == "__main__":
    print("--- 1. Multiplicación Rusa ---")
    print(f" 5 *  4 = {multiplicar(5, 4)}")
    print(f"-3 *  6 = {multiplicar(-3, 6)}")
    print(f" 7 * -2 = {multiplicar(7, -2)}")
    print(f"-4 * -4 = {multiplicar(-4, -4)}")