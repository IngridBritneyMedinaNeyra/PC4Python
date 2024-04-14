def contar_lineas_codigo(archivo):
    try:
        with open(archivo, "r") as f:
            lineas = f.readlines()
            lineas_limpias = [linea.strip() for linea in lineas if linea.strip() and not linea.strip().startswith("#")]
            return len(lineas_limpias)
    except FileNotFoundError:
        print("Error: Archivo no encontrado.")
        return None

def main():
    archivo = input("Ingrese la ruta del archivo .py: ")
    if archivo.endswith(".py"):
        lineas_codigo = contar_lineas_codigo(archivo)
        if lineas_codigo is not None:
            print(f"Número de líneas de código en '{archivo}': {lineas_codigo}")
    else:
        print("Error: El archivo no tiene extensión .py.")

if __name__ == "__main__":
    main()
