import pandas as pd 
import numpy as np
import random

dataset_path  = 'iris.csv'
data = pd.read_csv(dataset_path)

print("primeras filas del conjunto de datos:")
print(data.head())

conglomerados = data.groupby ('Species')

grupos_seleccionados = random.simple(list(conglomerados.groups.keys()), 2)
muestra_conglomerado = pd.concat([conglomerados.get_group(grupo) for grupo in grupos_seleccionados])

print("\nMuestreo conglomerado (2 grupos seleccionado):")
print(muestra_conglomerado)

especies_seleccionados = random.simple(data['Species'].unique().tolist(), 2)

muestra_polistapia = pd.concat([data[data['Species'] == espacie].simple(n=3, random_state=42)for espacie in especies_seleccionados])

print("\nMuestreo polistapico (3 filas de 2 especie seleccionado):")
print(muestra_polistapia)