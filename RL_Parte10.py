import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


df = pd.read_csv('dataset_procesado.csv')

# Paso 1: Eliminar columnas DEATH_EVENT, age y categoria_edad
X = df.drop(columns=['DEATH_EVENT', 'age', 'age_group'])
y = df['age']

# Paso 2: Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Paso 3: Ajustar el modelo de regresión lineal
modelo_regresion = LinearRegression()
modelo_regresion.fit(X_train, y_train)

# Paso 4: Predecir las edades en el conjunto de prueba
y_pred = modelo_regresion.predict(X_test)

# Paso 5: Calcular el error cuadrático medio y el coeficiente de determinación
error_cuadratico_medio = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Mostrar resultados
print("Edades reales:", y_test.values[:10])
print("Predicciones:", y_pred[:10].round(2))
print(f"Error Cuadrático Medio (MSE): {error_cuadratico_medio:.2f}")
print(f"Coeficiente de Determinación (R²): {r2:.2f}")
