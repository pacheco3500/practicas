import pandas as pd
import numpy as np 
import random

dataset_path ='iris.csv'
data = pd.read_csv(dataset_path)

print("Primerqs filas del conjunto de datos:")
print(data.head(10))

np.random.seed(42)
muestra_con_reposicion = data.sample(n=10, replace=True, random_state=42)
print("\nMuestreo con reposicion:")
print(muestra_con_reposicion)

np.random.seed(42)
muestra_sin_reposicion = data.sample(n=10, replace=False, random_state=42)
print("\nMuestreo sin reposicion:")
print(muestra_sin_reposicion)

random.seed(15)

total_population = 30
simple_size = 5

first_element = random.randint(1,total_population)
print(f"primer elemento seleccionado: {first_element}")

increment = total_population // simple_size
print(f"Incremento sistematico: {increment}")

systematic_sample = [(first_element + i *increment) % total_population for i in range (simple_size)]
print(f"Muestra sistematica: {systematic_sample}")

