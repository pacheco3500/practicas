import pandas as pd 
import numpy as np
import random
import matplotlib.pyplot as plt

dataset_path  = 'iris.csv'
data = pd.read_csv(dataset_path)

np.random.seed(1001)

petal_lengt = data["Petal.Length"]

num_samples = 500
sample_size = 10

sample_means = np.array([np.mean(np.random.choice(petal_lengt, sample_size, replace=True)) for _ in range(num_samples)])

mean_sample = np.mean(sample_means)

mean_population = np.mean(petal_lengt)

std_sample_means = np.std(sample_means, ddof=1)

std_population = np.std(petal_lengt, ddof=1)

std_theoretical = std_population / np.sqrt(sample_size)

print("Media de os valores medios de las muestras:", sample_means)
print("Media de la poblacion (Petal.length):", mean_population)
print("Desviacion estandar de los valores medios de las muestras:", std_sample_means)
print("Desviacion estandar teorica:", std_theoretical)

hist, bins = np.histogram(sample_means, bins=50)

plt.figure(figsize=(10, 6))
plt.hist(sample_means, bins=50, edgecolor='black', alpha=0.7)
plt.title("Histoggrama de las medias muestrales")
plt.xlabel("media de las muestra")
plt.ylabel("Frecuencia")
plt.legend()
plt.show()