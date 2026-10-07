def contar_caminos(n, m):
    # Caso Base: Si el tablero tiene solo 1 fila o 1 columna, 
    # la única forma de llegar es moviéndose todo recto (1 camino).
    if n == 1 or m == 1:
        return 1
        
    # Paso Recursivo: Sumar caminos moviéndose a la derecha (m-1) 
    # y caminos moviéndose abajo (n-1)
    return contar_caminos(n - 1, m) + contar_caminos(n, m - 1)

# === PRUEBAS DE EJECUCIÓN ===
if __name__ == "__main__":
    print("--- 4. Caminos en un Tablero ---")
    print(f"Caminos en tablero 2x2: {contar_caminos(2, 2)}")
    print(f"Caminos en tablero 3x3: {contar_caminos(3, 3)}")
    print(f"Caminos en tablero 3x4: {contar_caminos(3, 4)}")
    print(f"Caminos en tablero 4x4: {contar_caminos(4, 4)}")