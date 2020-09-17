import numpy as np
import matplotlib.pyplot as plt
import math

#=========pra quando tem a função===================
def f(x):
    return x**x

xs = [0.99, 1, 1.01]
pontos = [(x, f(x)) for x in xs]

#===================================================

#========pra quando tem a lista de pontos===========

# pontos = [(-1.22, 0.68), (-.86, 1.1), (-.48, 1.12)]

#===================================================

n = len(pontos)
def vandermond(pontos):
    xs, ys = zip(*pontos)
    A = [[x ** k for k in range(n)] for x in xs]
    B = ys
    a = np.linalg.solve(A, B)
    return a

a = vandermond(pontos)

def p(x):
    px = sum([a[k] * x ** k for k in range(n)])
    return px

def sign(x):
    if x < 0:
        return str(x)
    return f'+{x}'

def equation(pontos):
    eq = "p(x)="
    eq += "".join([f'{sign(a[k])}*x**{k}' for k in range(n)])
    return eq

eq = equation(pontos)
print(eq)

xs, ys = zip(*pontos)
left, right, step = min(xs), max(xs), 0.01

t = np.arange(left, right+step, step)
pt = [p(i) for i in t]
plt.scatter(xs, ys)
plt.plot(t, pt, label="poly", color="g")
plt.legend()
plt.show()
