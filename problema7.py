'pip install requests sqlite3'
import sqlite3
import requests

def obtener_tipo_cambio_anual():
    url = "https://apis.net.pe/api/tipo-cambio/2023"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción si la respuesta no es exitosa
        data = response.json()
        return data
    except requests.RequestException as e:
        print("Error al obtener el tipo de cambio:", e)
        return None

def crear_tabla(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS sunat_info (
                        fecha TEXT PRIMARY KEY,
                        compra REAL,
                        venta REAL
                    )''')

def insertar_datos(cursor, datos):
    for registro in datos:
        fecha = registro["fecha"]
        compra = registro["compra"]
        venta = registro["venta"]
        cursor.execute('''INSERT INTO sunat_info (fecha, compra, venta) VALUES (?, ?, ?)''', (fecha, compra, venta))

def mostrar_tabla(cursor):
    cursor.execute('''SELECT * FROM sunat_info''')
    for row in cursor.fetchall():
        print(row)

def main():
    # Obtener datos del API
    datos_tipo_cambio = obtener_tipo_cambio_anual()
    if datos_tipo_cambio is None:
        return

    # Conectar a la base de datos
    conexion = sqlite3.connect('base.db')
    cursor = conexion.cursor()

    # Crear tabla si no existe
    crear_tabla(cursor)

    # Insertar datos en la tabla
    insertar_datos(cursor, datos_tipo_cambio)

    # Guardar cambios y cerrar conexión
    conexion.commit()
    conexion.close()

    # Mostrar contenido de la tabla
    print("Contenido de la tabla 'sunat_info':")
    mostrar_tabla(cursor)

if __name__ == "__main__":
    main()
