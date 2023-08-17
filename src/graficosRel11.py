import matplotlib.pyplot as plt
import numpy as np

lux_I = [8.38, 7.87, 7.00, 5.91, 4.69, 3.45, 2.39, 1.54, 1.18]

del_lux = [0.08, 0.07, 0.07, 0.05, 0.04, 0.03, 0.02, 0.02, 0.01]

cos = [0.97, 0.88, 0.75, 0.59, 0.41, 0.25, 0.12, 0.03, 0]

del_cos = [0.21, 0.39, 0.52, 0.59, 0.59, 0.52, 0.39, 0.21, 0]

plt.errorbar(cos, lux_I, yerr=del_lux, xerr=del_cos, fmt='o', capsize=3)
plt.plot(cos, lux_I, color="#F60", label='$I(θ)$')

plt.xlabel('cos²(θ)', fontsize=12)
plt.ylabel('I [lux]', fontsize=12)
plt.title('I x cos²(θ)', fontsize=14)

plt.grid()
plt.legend()
plt.show()