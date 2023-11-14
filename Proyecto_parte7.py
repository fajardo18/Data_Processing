import pandas as pd
import matplotlib.pyplot as plt

# Cargar el DataFrame desde el archivo CSV
df = pd.read_csv("dataset_procesado.csv")

# Graficar la distribución de edades con un histograma
plt.figure(figsize=(8, 6))
plt.hist(df['age'], bins=10, edgecolor='k', alpha=0.6)
plt.title('Distribución de Edades')
plt.xlabel('Edad')
plt.ylabel('Cantidad')
plt.show()

# Definir los datos de los hombre y mujeres que son anemmicos, diabeticos, fumadores y muertos
df_anaemia = df.groupby("sex")["anaemia"].sum()
df_diabetes = df.groupby("sex")["diabetes"].sum()
df_smoking = df.groupby("sex")["smoking"].sum()
df_dead = df.groupby("sex")["DEATH_EVENT"].sum()


df_total_hom = [df_anaemia[1], df_diabetes[1], df_smoking[1], df_dead[1]]
df_total_muje = [df_anaemia[0], df_diabetes[0], df_smoking[0], df_dead[0]]
# # Definir las etiquetas del eje x
etiquetas = ["Anemicos", "Diabéticos", "Fumadores", "Muertos"]

# # Definir el ancho de las barras
ancho = 0.4

# # Crear el gráfico de barras
plt.bar(etiquetas, df_total_hom, width=-ancho, align='edge', label='Hombres')
plt.bar(etiquetas, df_total_muje, width=ancho, align='edge', label='Mujeres')


# # Añadir la leyenda
plt.legend()
plt.title('Histograma Agrupado por Sexo')
plt.xlabel('Categorias')
plt.ylabel('Cantidad')
plt.show()
