from datasets import load_dataset
import numpy as np

dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]
print(data)

# Parte 1.
age_list = dataset["train"]["age"]
age_array = np.array(age_list)
average_age = np.mean(age_array)
print(f"El promedio de edad de las personas participantes es: {average_age:.2f} años")

# Parte 2.

import pandas as pd

# Convertir el conjunto de datos en un DataFrame de Pandas
df = pd.DataFrame(dataset["train"])

# Separar en dos DataFrames: uno para perecidos (is_dead=1) y otro para no perecidos (is_dead=0)
df_perecidos = df[df["is_dead"] == 1]
df_no_perecidos = df[df["is_dead"] == 0]

# Calcular el promedio de edades para cada DataFrame
promedio_edad_perecidos = df_perecidos["age"].mean()
promedio_edad_no_perecidos = df_no_perecidos["age"].mean()

# Imprimir los resultados
print(f"Promedio de edades de personas que perecieron: {promedio_edad_perecidos:.2f} años")
print(f"Promedio de edades de personas que no perecieron: {promedio_edad_no_perecidos:.2f} años")

# Parte 3.

# Verificar los tipos de datos en cada columna del DataFrame
tipos_de_datos = df.dtypes

# Imprimir los tipos de datos
print("Tipos de datos en cada columna:")
print(tipos_de_datos)

# Filtrar el DataFrame para obtener hombres fumadores y mujeres fumadoras
hombres_fumadores = df[(df["is_male"] == 1) & (df["is_smoker"] == 1)]
mujeres_fumadoras = df[(df["is_male"] == 0) & (df["is_smoker"] == 1)]

# Calcular la cantidad de hombres fumadores y mujeres fumadoras
cantidad_hombres_fumadores = len(hombres_fumadores)
cantidad_mujeres_fumadoras = len(mujeres_fumadoras)

# Imprimir los resultados
print(f"Cantidad de hombres fumadores: {cantidad_hombres_fumadores}")
print(f"Cantidad de mujeres fumadoras: {cantidad_mujeres_fumadoras}")

# Parte 4.

import requests


def descargar_archivo_csv_desde_url(url, nombre_archivo):
    respuesta = requests.get(url)

    if respuesta.status_code == requests.codes.ok:
        with open(nombre_archivo, 'wb') as archivo:
            archivo.write(respuesta.content)
        print(f"Archivo descargado y guardado como {nombre_archivo}")
    else:
        print(f"Error al descargar el archivo. Código de respuesta: {respuesta.status_code}")


url = "https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv"
nombre_archivo = "heart_failure_dataset.csv"
descargar_archivo_csv_desde_url(url, nombre_archivo)
