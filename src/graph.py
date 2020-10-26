import pandas as pd
import matplotlib.pyplot as plt
import plotly.io as pio
import plotly.express as px

data_provincias = pd.read_csv('C:/Users/Toneti/Desktop/covid_analisis/datos_provincias.csv')
data_iso = pd.read_csv('C:/Users/Toneti/Desktop/covid_analisis/provinces_es.csv')

datos = pd.merge(data_provincias, data_iso, left_on='provincia_iso', right_on='code')
datos_col = datos[['fecha','num_casos','num_casos_prueba_pcr','num_casos_prueba_test_ac','num_casos_prueba_otras',\
                   'num_casos_prueba_desconocida','name']]

print(datos_col.head())

# Preparamos grafica
datos_1sep = datos_col[datos_col['fecha'] == '2020-09-01']

datos_alicante = datos_col[datos_col['name'] == 'Alacant']

fig = px.line(datos_alicante, x='fecha', y='num_casos', title='num casos Alicante')
fig.show()

#plt.plot(datos_alicante['fecha'], datos_alicante['num_casos'])
#plt.ylabel('num casos')
#plt.show()

pio.write_html(fig, file='primera_prueba.html', auto_open=True)
