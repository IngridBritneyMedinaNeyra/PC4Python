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

def calcular_costo_bitcoins(bitcoins):
    precio_usd = obtener_precio_bitcoin()
    if precio_usd is not None:
        costo_usd = bitcoins * precio_usd
        return costo_usd
    else:
        return None

def main():
    try:
        cantidad_bitcoins = float(input("Ingrese la cantidad de bitcoins que posee: "))
        costo_usd = calcular_costo_bitcoins(cantidad_bitcoins)
        if costo_usd is not None:
            print(f"El costo actual de {cantidad_bitcoins} bitcoins es: ${costo_usd:,.4f}")
    except ValueError:
        print("Error: Por favor ingrese un número válido.")

if __name__ == "__main__":
    main()

