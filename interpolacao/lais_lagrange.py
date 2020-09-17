# pontos = [(1, 2), (2, 5), (3, -1), (4, 2)]

# pontos = [(-2.5, 0.94), (-2.0, -3.08), (-1.5, 5.33), (-1.0, 2.57), (-0.5, -5.94), (0.0, 4.39), (0.5, -2.35), (1.0, 0.17), (1.5, 5.38),
# (2.0, -1.13), (2.5, -2.63)]
#
# pontos = [(-2.5, -5.6), (-2.0, -4.03), (-1.5, -0.4), (-1.0, -1.12), (-0.5, 1.51), (0.0, 2.98), (0.5, -4.59), (1.0, 0.56), (1.5, -4.43),
# (2.0, -5.53), (2.5, 2.14), (3.0, 4.02), (3.5, 0.85), (4.0, 1.37), (4.5, 5.26), (5.0, 2.79), (5.5, 5.16), (6.0, -2.28), (6.5, -2.9),
# (7.0, -0.61), (7.5, -3.93), (8.0, 2.04), (8.5, 5.61), (9.0, -2.09), (9.5, 1.55), (10.0, -0.59), (10.5, -5.47), (11.0, -5.5),
# (11.5, 2.64), (12.0, 2.0), (12.5, 5.1)]

# pontos = [(-1.22, 0.68), (-.86, 1.1), (-.48, 1.12)]

#modificado =================================
# função para interpolar
def f(x):
    return x**x

xs = [0.99, 1, 1.01]
pontos = [(x, f(x)) for x in xs]
print(*pontos)
#============================================

# pontos = [(-2.5, 0.89), (-2.0, -1.18), (-1.5, 1.88), (-1.0, 4.06), (-0.5, 1.21)]
# pontos = [(1, 2), (2, 5), (3, -1), (4, 2), (3.1, 3), (1.2, 8)]
# pontos = [(22, 10), (19, 10), (99, 1)]

# pontos = [(-2.5, -3.99), (-2.0, -5.26), (-1.5, 0.54), (-1.0, -4.29), (-0.5, -2.59), (0.0, -0.95), (0.5, -0.15)]
#realiza a multiplicação de uma lista
def prod(lista):
    p = 1
    for i in lista:
        p *= i
    return p

def lagrange(pontos, x):
    # retorna o valor do polinômio de Lagrange que interpola
    # a lista 'pontos' calculado no ponto x
    xs, ys = zip(*pontos)
    soma = 0
    for k, y in enumerate(ys):
        xk = xs[k]
        Lk_numerador = prod([x - xi for i, xi in enumerate(xs) if i != k])
        Lk_denominador = prod([xk - xi for i, xi in enumerate(xs) if i != k])
        soma += y * (Lk_numerador / Lk_denominador)
    return soma

def p(x):
    return lagrange(pontos, x)

import matplotlib.pyplot as plt
import numpy as np



# usado para desenhar o gráfico da função
# pontos no intervalo [-1, 1]
n = len(pontos)
xs, ys = zip(*pontos)

a = min(xs) -1
b = max(xs) +1

print(a, b)
t = np.arange(a, b, 0.1)
# t = [a + i * (b / 999) for i in range(1000)]

# ft = [f(i) for i in t]
# plt.plot(t, ft, label="gráfico de $f(x)=\\frac{1}{1 + 25x^2}$")
# plt.show()

# polinômio interpolador
# lista de pontos no intervalo [-1, 1]

# xs = [-1 + i * (2 / (n - 1)) for i in range(n)]
# ys = [f(i) for i in xs]
# pontos = [(x, f(x)) for x in xs]

# plotar os 'pontos'
plt.scatter(xs, ys)

# plotar o gráfico de p(x)
pt = [p(i) for i in t]
plt.plot(t, pt, label="polinômio interpolador")
plt.legend()
plt.title(f"{n} pontos")
# Fenômeno de Runge
# plt.savefig(f'{n}pontos', dpi=300)
plt.show()
