import matplotlib.pyplot as plt
import numpy as np
# y' = 2 * y + x + 1, y(x0) = y0
# possui única solução pelo EXU

x0, y0 = 0, 2
h = 0.1 # tamanho do passo
n = 50

def f(x, y):
    return x**2+y+1

def solucao_do_pvi(x):
    return -x**2 - 2*x + 5 * np.exp(x) - 3

print("Calculando a aproximação de Euler, Heun, Ralston e Serpson para y′=x2+y+1,y(0)=2.")
print("O tamanho do gap entre os pontos é h=",h)
print("O número de iteraçõe usado em cada método será n=",n)

def euler(f, x0, y0, h):
    x = {0: x0}
    y = {0: y0}
    for i in range(1, n):
        x[i] = x0 + i * h
        y[i] = y[i - 1] + f(x[i - 1], y[i - 1]) * h
    return x, y

def heun(f, x0, y0, h):
    x = {i: x0 + i * h for i in range(n)}
    y = {0: y0}
    for k in range(n - 1):
        m1 = f(x[k], y[k])
        m2 = f(x[k] + h, y[k] + m1 * h)
        y[k + 1] = y[k] + (h / 2) * (m1 + m2)
    return x, y

def ralston(f, x0, y0, h):
    x = {i: x0 + i * h for i in range(n)}
    y = {0: y0}
    for k in range(n - 1):
        m1 = f(x[k], y[k])
        m2 = f(x[k] + h, y[k] + m1 * h)
        y[k + 1] = y[k] + (h / 3) * (1 * m1 + 2 * m2)
    return x, y

def rk2(f, x0, y0,c2, h):
    # c1 + c2 = 1 --> c1 = 1 - c2, c2 > 0
    c1 = 1 - c2
    x = {i: x0 + i * h for i in range(n)}
    y = {0: y0}
    for k in range(n - 1):
        m1 = f(x[k], y[k])
        m2 = f(x[k] + h, y[k] + m1 * h)
        y[k + 1] = y[k] + h * (c1 * m1 + c2 * m2)
    return x, y

xs, ys = euler(f, x0, y0, h)
x = [v for _, v in xs.items()]
y = [v for _, v in ys.items()]

hxs, hys = heun(f, x0, y0, h)
hx = [v for _, v in hxs.items()]
hy = [v for _, v in hys.items()]

rxs, rys = ralston(f, x0, y0, h)
rx = [v for _, v in rxs.items()]
ry = [v for _, v in rys.items()]


print("Fazendo para qualquer método de ordem 2, com c2=1/99. Este método é conhecido na comunidade acadêmica de Matemática como Método Serpson")
sxs, sys = rk2(f, x0, y0,1/99, h)
sx = [v for _, v in sxs.items()]
sy = [v for _, v in sys.items()]

t = np.linspace(x0, x0 + n * h, 100)

plt.scatter(x, y, label="Euler")
plt.scatter(hx, hy, label="Heun")
plt.scatter(rx, ry, label="Ralston")
# plt.scatter(sx, sy, label="Serpson")
plt.plot(t, solucao_do_pvi(t))
plt.legend()
plt.show()
