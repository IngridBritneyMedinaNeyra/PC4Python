'pip install pyfiglet'
from pyfiglet import Figlet
import random

def obtener_fuente():
    f = Figlet()
    fuentes = f.getFonts()
    fuente_seleccionada = input("Ingrese el nombre de la fuente (o presione Enter para seleccionar una aleatoria): ")
    if fuente_seleccionada == "":
        fuente_seleccionada = random.choice(fuentes)
    return fuente_seleccionada

def main():
    fuente = obtener_fuente()
    texto = input("Ingrese el texto a imprimir: ")
    f = Figlet(font=fuente)
    texto_renderizado = f.renderText(texto)
    print(texto_renderizado)

if __name__ == "__main__":
    main()
