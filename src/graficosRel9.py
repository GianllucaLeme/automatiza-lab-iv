import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

comp_lambda = np.array([623e-9, 579e-9, 546e-9, 436e-9])
indice_n = np.array([1.513, 1.519, 1.524, 1.536])
indice_erro = [0.001, 0.001, 0.001, 0.001]

# Função de interpolação para gerar uma curva suave (cubic)
interp_func = interp1d(comp_lambda, indice_n, kind='cubic')

# Definindo o novo conjunto de pontos para a curva suave
comp_lambda_smooth = np.linspace(comp_lambda.min(), comp_lambda.max(), 1000)
indice_n_smooth = interp_func(comp_lambda_smooth)

plt.errorbar(comp_lambda, indice_n, yerr=indice_erro, fmt='o', capsize=3)
plt.plot(comp_lambda_smooth, indice_n_smooth, color="#F60", label='$n$ (suave)')

plt.xlabel('Comprimento de Onda [m]', fontsize=12)
plt.ylabel('Índice de Refração', fontsize=12)
plt.title('Gráfico de $n (λ)$', fontsize=14)

plt.grid()
plt.legend()
plt.show()
