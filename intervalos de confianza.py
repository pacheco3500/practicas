import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

mu_0 = 75
n = 40
x_bar = 72
sigma = 10
alpha = 0.05

z = (x_bar - mu_0) / (sigma / np.sqrt(n))

z_critical = stats.norm.ppf(alpha)

x = np.linspace(mu_0 - 4 * (sigma/np.sqrt(n)), mu_0 + 4 * (sigma/np.sqrt(n)), 108)
y = stats.norm.pdf(x, mu_0, sigma / np.sqrt(n))

plt.figure(figsize=(8, 5))
plt.plot(x, y, color='orange')

x_fill = np.linspace(-4, z_critical, 100) * (sigma / np.sqrt(n)) + mu_0
y_fill = stats.norm.pdf(x_fill, mu_0, sigma / np.sqrt(n))
plt.fill_between(x_fill, y_fill, color='red', alpha=0.3)

plt.xlabel('Puntaje')
plt.ylabel('Densidad de probabilidad')
plt.title('Contraste de Hipótesis')
plt.legend()
plt.grid()

plt.show()

if z < z_critical:
    decision = "Rechazamos HO: La media del puntaje es menor a 75."
else:
    decision = "No rechazamos HO: No hay suficiente evidencia para decir que la media es menor a 75."
print(decision)