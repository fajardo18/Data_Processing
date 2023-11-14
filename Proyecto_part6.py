import requests
import csv
import pandas as pd
import sys


def descargar_y_guardar_csv(url, nombre_archivo):
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


if len(sys.argv) != 2:
    sys.exit(1)

url_datos = sys.argv[1]
nombre_archivo = "heart_failure_clinical_records_dataset.csv"

# Llamar a la función para descargar y guardar los datos en un archivo CSV
descargar_y_guardar_csv(url_datos, nombre_archivo)

# Leer el archivo CSV y realizar las operaciones de limpieza
df = pd.read_csv(nombre_archivo)
resultado = limp(df)

print("Procesamiento completo. Resultado guardado en 'dataset_procesado.csv'.")

# Este script puede ejecutarse desde la línea de comandos proporcionando la URL como argumento
# python proyecto_part6.py
# https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv
