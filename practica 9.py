import numpy as np 
import pandas as pd 
import scipy.stats as stats 
import matplotlib.pyplot as plt

archivo = "Titanic-Dataset.csv"
df = pd.read_csv(archivo)

muestra = df['Fare'].values 
n= len(muestra)

X_bar = np.mean(muestra)
S2_X = np.var(muestra, ddof=1) 
S_X = np.sqrt(S2_X)

sigma_x = S_X
sigma_x2 = sigma_x**2

chi2_valor = (n - 1) * S2_X / sigma_x2
probabilidad = stats.chi2.cdf(chi2_valor, df=n - 1)

print(f"Varianza muestral: {S2_X:.4f}")
print(f"Desviacioj tipica muestrak: {S_X:.4f}")
print(f"probabilidad P(S_X < 2.5): {S_X:.4f}")

plt.figure(figsize=(8, 4))
plt.hist(muestra, bins=15, color='purple', edgecolor='black', alpha=0.5)

plt.title("Histograma de la columna 'Fare' de Titanic Dataset.csv")
plt.xlabel ("Valores de 'Tarifa'")
plt.ylabel ("Frecuencia")

plt.show()