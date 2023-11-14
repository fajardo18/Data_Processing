import matplotlib.pyplot as plt

# Categorías y valores para cada gráfico
categorias_anemia = ['No Anémicos', 'Anémicos']
valores_anemia = df['anaemia'].value_counts()

categorias_diabetes = ['No Diabéticos', 'Diabéticos']
valores_diabetes = df['diabetes'].value_counts()

categorias_fumadores = ['No Fumadores', 'Fumadores']
valores_fumadores = df['smoking'].value_counts()

categorias_fallecidos = ['Vivos', 'Fallecidos']
valores_fallecidos = df['DEATH_EVENT'].value_counts()


plt.figure(figsize=(8, 5))

# Subplot 1: Anemia
plt.subplot(2, 2, 1)
plt.pie(valores_anemia, labels=categorias_anemia, autopct='%1.1f%%', startangle=90)
plt.title('Distribución de Anémicos')

# Subplot 2: Diabetes
plt.subplot(2, 2, 2)
plt.pie(valores_diabetes, labels=categorias_diabetes, autopct='%1.1f%%', startangle=90)
plt.title('Distribución de Diabéticos')

# Subplot 3: Fumadores
plt.subplot(2, 2, 3)
plt.pie(valores_fumadores, labels=categorias_fumadores, autopct='%1.1f%%', startangle=90)
plt.title('Distribución de Fumadores')

# Subplot 4: Fallecidos
plt.subplot(2, 2, 4)
plt.pie(valores_fallecidos, labels=categorias_fallecidos, autopct='%1.1f%%', startangle=90)
plt.title('Distribución de Personas Fallecidas')

plt.tight_layout()
plt.show()
