import numpy as np
import scipy.stats as stats

n = 500
sigma_x = 100
sigma_x2 = sigma_x**2

np.random.seed(42)
muestra = np.random.normal(loc=0, scale=sigma_x, size=n)

X_bar = np.mean(muestra)

S2_X = np.var(muestra, ddof=1)

S_X = np.sqrt(S2_X)

ch2_valor = (n - 1) * S2_X / sigma_x2
probabilidad = stats.chi2.cdf(ch2_valor, df=n - 1)

print(f"Varianza muestral: {S2_X:.4f}")
print(f"Desviacion tipica muestral: {S_X:.4f}")
print(f"Probabilidad P(S_X < 2.5): {probabilidad:.4f}")