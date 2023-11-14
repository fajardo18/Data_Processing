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
import csv


def descargar_y_guardar_csv(url):
    # Realizar la solicitud GET
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Escribir la respuesta en un archivo CSV usando csv.writer
        with open(nombre_archivo, 'w', newline='') as archivo_csv:
            csv_writer = csv.writer(archivo_csv)

            # Decodificar y dividir las líneas del contenido de la respuesta
            lines = response.content.decode('utf-8').splitlines()

            # Utilizar csv.reader para escribir las líneas en el archivo CSV
            for line in csv.reader(lines):
                csv_writer.writerow(line)

        print(f"Descarga exitosa. Los datos han sido guardados en '{nombre_archivo}'.")
    else:
        print(f"Error al descargar los datos. Código de estado: {response.status_code}")


# URL de los datos
url_datos = "https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv"

# Llamar a la función para descargar y guardar los datos en un archivo CSV
descargar_y_guardar_csv(url_datos, "heart_failure_clinical_records_dataset.csv")


# Parte 5.


def limp(df: pd.DataFrame) -> pd.DataFrame:

    columns_with_missing_values = df.columns[df.isna().any()]
    for column in columns_with_missing_values:
        mean_value = df[column].mean()
        df[column] = df[column].fillna(mean_value)

    def iqr_c(column):
        q1 = column.quantile(0.25)
        q3 = column.quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        return (column >= lower_bound) & (column <= upper_bound)

    for column in df.select_dtypes(include='number'):
        df = df[iqr_c(df[column])]

    def categorize_age(x):
        if x <= 12:
            return 'Niño'
        elif x <= 19:
            return 'Adolescente'
        elif x <= 39:
            return 'Joven adulto'
        elif x <= 59:
            return 'Adulto'
        else:
            return 'Adulto mayor'

    df['age_group'] = df['age'].apply(categorize_age)
    df.to_csv("dataset_procesado.csv", index=False)
    return df


df = pd.read_csv('heart_failure_clinical_records_dataset.csv')
resultado = limp(df)

