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
