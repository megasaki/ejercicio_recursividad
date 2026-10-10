class ExploradorRecursivo:
    """
    Clase para recorrer y analizar un sistema de archivos simulado
    mediante un diccionario anidado utilizando recursividad.
    """

    def __init__(self, sistema_archivos):
        # Almacenamos el sistema de archivos raíz en la instancia
        self.sistema_raiz = sistema_archivos

    def imprimir_arbol(self, sistema=None, nivel=0):
        """
        Recorre el diccionario y muestra la jerarquía con indentación visual.
        """
        # Inicialización para la primera llamada externa
        if sistema is None:
            sistema = self.sistema_raiz

        for nombre, contenido in sistema.items():
            # Generamos la indentación basada en el nivel recursivo actual
            indentacion = "    " * nivel
            
            # Caso Base: El contenido NO es un diccionario (es un archivo/hoja)
            if not isinstance(contenido, dict):
                print(f"{indentacion}{nombre} ({contenido})")
            
            # Paso Recursivo: El contenido ES un diccionario (es una carpeta/rama)
            else:
                print(f"{indentacion}{nombre}/")
                # Llamamos a la función incrementando el nivel de indentación
                self.imprimir_arbol(contenido, nivel + 1)

    def buscar_archivo(self, nombre_buscar, sistema=None, ruta_actual=""):
        """
        Realiza una búsqueda profunda para encontrar la ruta de un archivo.
        Retorna la ruta completa en formato string o None si no existe.
        """
        if sistema is None:
            sistema = self.sistema_raiz

        for nombre, contenido in sistema.items():
            # Construimos la ruta dinámica agregando el nodo actual
            nueva_ruta = f"{ruta_actual}/{nombre}" if ruta_actual else nombre
            
            # Caso Base 1: Encontramos el archivo y verificamos que no sea carpeta
            if nombre == nombre_buscar and not isinstance(contenido, dict):
                return nueva_ruta
                
            # Paso Recursivo: Si es una carpeta, entramos a buscar en su interior
            if isinstance(contenido, dict):
                resultado_busqueda = self.buscar_archivo(nombre_buscar, contenido, nueva_ruta)
                
                # Caso Base 2 (implícito): Si la recursividad encontró algo adentro, 
                # propagamos esa ruta hacia arriba para no perderla.
                if resultado_busqueda:
                    return resultado_busqueda
                    
        # Caso Base 3: Terminó el ciclo en este nivel y no se encontró nada
        return None

    def contar_archivos(self, sistema=None):
        """
        Cuenta exclusivamente los nodos hoja (archivos), ignorando carpetas.
        """
        if sistema is None:
            sistema = self.sistema_raiz

        total_archivos = 0

        for nombre, contenido in sistema.items():
            # Caso Base: Es un archivo, sumamos 1 al contador de este nivel
            if not isinstance(contenido, dict):
                total_archivos += 1
                
            # Paso Recursivo: Es una carpeta, sumamos lo que devuelva su interior
            else:
                total_archivos += self.contar_archivos(contenido)

        return total_archivos


# === PRUEBAS DE EJECUCIÓN ===
if __name__ == "__main__":
    sistema_prueba = {
        "Documentos": {
            "apuntes.txt": "10kb",
            "fotos": {
                "vacaciones.png": "2mb",
                "perro.jpg": "1mb"
            }
        },
        "sistema.dll": "500kb"
    }

    explorador = ExploradorRecursivo(sistema_prueba)

    print("--- 1. Imprimir Árbol ---")
    explorador.imprimir_arbol()

    print("\n--- 2. Buscar Archivo ---")
    objetivo_1 = "perro.jpg"
    objetivo_2 = "sistema.dll"
    objetivo_3 = "secreto.txt"
    
    print(f"Buscando '{objetivo_1}': {explorador.buscar_archivo(objetivo_1)}")
    print(f"Buscando '{objetivo_2}': {explorador.buscar_archivo(objetivo_2)}")
    print(f"Buscando '{objetivo_3}': {explorador.buscar_archivo(objetivo_3) or 'No encontrado'}")

    print("\n--- 3. Contar Archivos ---")
    cantidad = explorador.contar_archivos()
    print(f"Total de archivos en el sistema: {cantidad}")