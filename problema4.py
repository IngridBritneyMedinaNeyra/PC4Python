'pip install requests'
import requests

def obtener_precio_bitcoin():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  # Lanza una excepción si la respuesta no es exitosa
        data = response.json()
        precio_usd = data["bpi"]["USD"]["rate_float"]
        return precio_usd
    except requests.RequestException as e:
        print("Error al obtener el precio de Bitcoin:", e)
        return None

def guardar_precio_en_archivo(precio):
    try:
        with open("bitcoin_prices.txt", "a") as archivo:
            archivo.write(f"{precio}\n")
            print("Precio de Bitcoin guardado en el archivo.")
    except IOError as e:
        print("Error al guardar el precio de Bitcoin en el archivo:", e)

def main():
    precio = obtener_precio_bitcoin()
    if precio is not None:
        guardar_precio_en_archivo(precio)

if __name__ == "__main__":
    main()
