import pandas as pd
import numpy as np
from sklearn.manifold import TSNE
import plotly.express as px


df = pd.read_csv('dataset_procesado.csv')

# Elimina las columnas especificadas
columns_to_drop = ['DEATH_EVENT', 'age_group']
X = df.drop(columns=columns_to_drop).values

# Extrae la columna objetivo (DEATH_EVENT)
y = df['DEATH_EVENT'].values

# Aplica TSNE para reducción de dimensionalidad a 3 componentes
X_embedded = TSNE(n_components=3, learning_rate='auto', init='random', perplexity=3).fit_transform(X)

# Crea un DataFrame con las coordenadas y la etiqueta de clase
df_embedded = pd.DataFrame({'X': X_embedded[:, 0], 'Y': X_embedded[:, 1], 'Z': X_embedded[:, 2], 'label': y})

# Crea un gráfico de dispersión 3D con Plotly
fig = px.scatter_3d(df_embedded, x='X', y='Y', z='Z', color='label',
                    color_discrete_map={0: 'blue', 1: 'red'},
                    title='TSNE Visualization of Data',
                    labels={'label': 'DEATH_EVENT'})

fig.show()
