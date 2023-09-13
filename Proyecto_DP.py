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
