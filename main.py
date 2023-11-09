from Proyecto_DP import procesar_datos
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python procesar_datos.py <URL>")
    else:
        url = sys.argv[1]
        procesar_datos(url)