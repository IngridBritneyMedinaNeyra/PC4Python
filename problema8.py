'pip install requests sqlite3'
import sqlite3
import requests

def obtener_precio_bitcoin():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  # Lanza una excepción si la respuesta no es exitosa
        data = response.json()
        precio_usd = data["bpi"]["USD"]["rate_float"]
        precio_gbp = data["bpi"]["GBP"]["rate_float"]
        precio_eur = data["bpi"]["EUR"]["rate_float"]
        return precio_usd, precio_gbp, precio_eur
    except requests.RequestException as e:
        print("Error al obtener el precio de Bitcoin:", e)
        return None, None, None

def obtener_tipo_cambio_pen():
    try:
        response = requests.get("https://api.sunat.cloud/cambio?fecha=now")
        response.raise_for_status()
        data = response.json()
        tipo_cambio_pen = data["cambio"]["rate"]
        return tipo_cambio_pen
    except requests.RequestException as e:
        print("Error al obtener el tipo de cambio PEN:", e)
        return None

def crear_tabla_bitcoin(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS bitcoin (
                        fecha TEXT PRIMARY KEY,
                        precio_usd REAL,
                        precio_gbp REAL,
                        precio_eur REAL,
                        precio_pen REAL
                    )''')

def insertar_datos_bitcoin(cursor, precio_usd, precio_gbp, precio_eur, precio_pen):
    cursor.execute('''INSERT INTO bitcoin (fecha, precio_usd, precio_gbp, precio_eur, precio_pen) 
                      VALUES (date('now'), ?, ?, ?, ?)''', (precio_usd, precio_gbp, precio_eur, precio_pen))

def calcular_compra_10_bitcoins(cursor):
    cursor.execute('''SELECT precio_pen, precio_eur FROM bitcoin WHERE fecha = date('now')''')
    fila = cursor.fetchone()
    if fila:
        precio_pen = fila[0]
        precio_eur = fila[1]
        precio_compra_pen = precio_pen * 10
        precio_compra_eur = precio_eur * 10
        print(f"Precio de compra de 10 bitcoins en PEN: {precio_compra_pen} PEN")
        print(f"Precio de compra de 10 bitcoins en EUR: {precio_compra_eur} EUR")
    else:
        print("No se encontraron datos de Bitcoin para el día de hoy.")

def main():
    # Obtener precios de Bitcoin y tipo de cambio PEN
    precio_usd, precio_gbp, precio_eur = obtener_precio_bitcoin()
    tipo_cambio_pen = obtener_tipo_cambio_pen()
    if precio_usd is None or precio_gbp is None or precio_eur is None or tipo_cambio_pen is None:
        return

    # Conectar a la base de datos
    conexion = sqlite3.connect('base.db')
    cursor = conexion.cursor()

    # Crear tabla 'bitcoin' si no existe
    crear_tabla_bitcoin(cursor)

    # Calcular precio en PEN
    precio_pen = precio_usd * tipo_cambio_pen

    # Insertar datos en la tabla 'bitcoin'
    insertar_datos_bitcoin(cursor, precio_usd, precio_gbp, precio_eur, precio_pen)

    # Consultar y calcular compra de 10 bitcoins en PEN y EUR
    calcular_compra_10_bitcoins(cursor)

    # Guardar cambios y cerrar conexión
    conexion.commit()
    conexion.close()

if __name__ == "__main__":
    main()
