'pip install zipfile requests'
import requests
import zipfile
from io import BytesIO
import os

def descargar_imagen(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except requests.RequestException as e:
        print("Error al descargar la imagen:", e)
        return None

def guardar_imagen(nombre_archivo, contenido):
    with open(nombre_archivo, "wb") as archivo:
        archivo.write(contenido)
        print(f"La imagen ha sido guardada como '{nombre_archivo}'.")

def comprimir_zip(archivo_origen, nombre_zip):
    with zipfile.ZipFile(nombre_zip, "w") as zipf:
        zipf.write(archivo_origen, os.path.basename(archivo_origen))
        print(f"El archivo '{archivo_origen}' ha sido comprimido como '{nombre_zip}'.")

def descomprimir_zip(nombre_zip, carpeta_destino):
    with zipfile.ZipFile(nombre_zip, "r") as zipf:
        zipf.extractall(carpeta_destino)
        print(f"El archivo '{nombre_zip}' ha sido descomprimido en la carpeta '{carpeta_destino}'.")

def main():
    url_imagen = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    contenido_imagen = descargar_imagen(url_imagen)
    if contenido_imagen:
        guardar_imagen("imagen_descargada.jpg", contenido_imagen)
        comprimir_zip("imagen_descargada.jpg", "imagen_comprimida.zip")
        descomprimir_zip("imagen_comprimida.zip", "imagen_descomprimida")

if __name__ == "__main__":
    main()
