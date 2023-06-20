import sympy as sp

# Dados colhidos no laboratório
(Res1, res2, L_ind, Cap) = (121.0, 11.5, 37.5e-3, 1.64e-6)

omega = [629.575,  1256.637, 1886.841, 2513.274, 3141.593, 3764.256, 4084.699,
         4399.486, 5026.548, 5654.867, 6283.185, 6905.221, 7546.106, 8174.424]

del_omega = [18.209,  29.022, 32.717,  58.044, 45.346,  65.100, 76.655,
             88.926, 116.082, 146.920, 181.383, 219.070, 104.646, 122.799]

del_R = 0.009 * Res1 + 0.2
del_r = 0.009 * res2 + 0.2
del_L = L_ind * 0.05 + 1e-4
del_C = Cap * 0.019 + 2 * 0.01e-6

# Definindo as variáveis simbólicas
(R, r, w, L, C) = (sp.Symbol('R'), sp.Symbol('r'), sp.Symbol('w'), sp.Symbol('L'), sp.Symbol('C'))

# Definindo a função
Z = ((R+r) ** 2 + (w*L - 1/(w*C)) ** 2) ** 0.5

# Calculando as derivadas
Z_derivada_R = sp.diff(Z, R)
Z_derivada_r = sp.diff(Z, r)
Z_derivada_w = sp.diff(Z, w)
Z_derivada_L = sp.diff(Z, L)
Z_derivada_C = sp.diff(Z, C)

# Função da incerteza de Z
delta_Z = ((Z_derivada_R * del_R)**2 + (Z_derivada_r * del_r)**2 + (Z_derivada_w * 5)
           ** 2 + (Z_derivada_L * del_L)**2 + (Z_derivada_C * del_C)**2) ** 0.5

# Exibindo a lista de incertezas da impedância Z

index = 0
del_Z = []
while index < len(omega):
    resultado = delta_Z.subs([(R, Res1), (r, res2), (w, omega[index]), (L, L_ind), (C, Cap)])
    del_Z.append(resultado)
    print("ΔZ[" + str(index+1) + "] = " + str(resultado))
    index += 1

print()
print(del_Z)
print()

# Após esse processo, o vetor 'del_Z' é jogado para o arquivo .js, onde o array é trabalhado com as regras de arrendodamento do próprio JavaScript
