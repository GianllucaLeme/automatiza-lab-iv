import matplotlib.pyplot as plt
import numpy as np

f = [100.2, 200.0, 300.3, 400.0, 500.0, 599.1, 650.1,
     700.2, 800.0, 900.0, 1000.0, 1099.0, 1201.0, 1301.0]
del_f = [2.90, 4.62, 5.21, 9.24, 7.22, 10.36, 12.20,
         14.15, 18.48, 23.38, 28.87, 34.87, 16.66, 19.54]

Vef_vr = [454e-3, 919e-3, 1.39, 1.82, 2.02, 2.32,
          2.42, 2.46, 2.24, 2.01, 1.92, 1.81, 1.53, 1.42]
del_vef = [0.06, 0.12, 0.12, 0.23, 0.23, 0.23,
           0.23, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12]

maximo = np.argmax(Vef_vr)
ponto_maximo = (f[maximo], Vef_vr[maximo])
color_max = '#C00'
color_error = '#6557D2'

plt.errorbar(f, Vef_vr, yerr=del_vef, fmt='o', color=color_error, capsize=3)
plt.errorbar(f, Vef_vr, xerr=del_f, fmt='o', color=color_error, capsize=3)

plt.errorbar(*ponto_maximo, yerr=del_vef[7],
             fmt='o', color=color_max, capsize=3)
plt.errorbar(*ponto_maximo, xerr=del_f[7], fmt='o', color=color_max, capsize=3)

plt.scatter(*ponto_maximo, color=color_max, label="$P_{max}=(700,2; 2,46)$")

plt.plot(f, Vef_vr, color="#F60", label='$V_{ef}$')
plt.axvline(ponto_maximo[0], 0, 0.82, color=color_max,
            linestyle='--', linewidth=0.75)
plt.axhline(ponto_maximo[1], 0, 0.5, color=color_max,
            linestyle='--', linewidth=0.75)

plt.xlabel('Frequência [Hz]', fontsize=12)
plt.ylabel('Vef/Vr [V]', fontsize=12)
plt.title('Gráfico de $V_{ef} (f)$', fontsize=14)

plt.grid()
plt.legend()

print("Frequencia experimental maxima: " + str(ponto_maximo[0]) + " [Hz]")
plt.show()
