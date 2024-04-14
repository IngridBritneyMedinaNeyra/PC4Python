def guardar_tabla_multiplicar(numero):
    try:
        with open(f"tabla-{numero}.txt", "w") as archivo:
            for i in range(1, 11):
                archivo.write(f"{numero} x {i} = {numero * i}\n")
        print(f"Tabla de multiplicar del {numero} guardada en 'tabla-{numero}.txt'")
    except IOError as e:
        print("Error al guardar la tabla de multiplicar:", e)

def mostrar_tabla_multiplicar(numero):
    try:
        with open(f"tabla-{numero}.txt", "r") as archivo:
            print(f"Tabla de multiplicar del {numero}:\n")
            print(archivo.read())
    except FileNotFoundError:
        print(f"No existe el archivo 'tabla-{numero}.txt'.")

def mostrar_linea_tabla_multiplicar(numero, linea):
    try:
        with open(f"tabla-{numero}.txt", "r") as archivo:
            lineas = archivo.readlines()
            if len(lineas) >= linea:
                print(f"Línea {linea}: {lineas[linea - 1]}")
            else:
                print(f"No existe la línea {linea} en 'tabla-{numero}.txt'.")
    except FileNotFoundError:
        print(f"No existe el archivo 'tabla-{numero}.txt'.")

def main():
    while True:
        print("\n1. Guardar tabla de multiplicar.")
        print("2. Mostrar tabla de multiplicar.")
        print("3. Mostrar línea de la tabla de multiplicar.")
        print("4. Salir.")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            if 1 <= numero <= 10:
                guardar_tabla_multiplicar(numero)
            else:
                print("Número fuera de rango.")
        elif opcion == "2":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            if 1 <= numero <= 10:
                mostrar_tabla_multiplicar(numero)
            else:
                print("Número fuera de rango.")
        elif opcion == "3":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            if 1 <= numero <= 10:
                linea = int(input("Ingrese el número de línea a mostrar: "))
                mostrar_linea_tabla_multiplicar(numero, linea)
            else:
                print("Número fuera de rango.")
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
