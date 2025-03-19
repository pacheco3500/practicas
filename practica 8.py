import   numpy as np
import pandas   as pd 
import scipy.stats as stats
import matplotlib.pyplot as plt

archivo = "worldcup.csv"
df = pd.read_csv(archivo)

muestra = df['Time'].values
n = len(muestra)

X_bar = np.mean(muestra)
S2_X = np.var(muestra, ddof=1)
S_X = np.sqrt(S2_X)

sigma_x = S_X
sigma_x2 = sigma_x**2 

chi2_valor = (n - 1) * S2_X / sigma_x2
probabilidad = stats.chi2.cdf(chi2_valor, df=n - 1)

print(f"varianza muestra: {S2_X:.4f}")
print(f"Desviacion tipica muestral: {S_X:.4f}")
print(f"Probabilidad P(S_X < 2.5): {probabilidad:.4f}")

plt.figure(figsize=(9,5))
plt.hist(muestra, bins=15, color='green', edgecolor='black', alpha=0.8)

plt.title("Histograma de la columna ''time del archivoworldcup.csv")
plt.xlabel("Valores de 'time'")
plt.ylabel("Frecuencia")

plt.show()