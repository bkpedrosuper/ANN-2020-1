# uma função qualquer
import math
def f(x):
    return x**3+x**2 + 0.001

# derivada de f
def df(x):
    return 3*x**2 + 2*x


chosen = 0
x0 = 2
n = 10
itr = {}
itr[0] = x0
print("O número de iterações é", n)
for i in range(1, n):
    itr[i] = x0 - f(x0) / df(x0)
    x0 = itr[i]

for k, v in itr.items():
    print(k, v)
    chosen = v
print("a raiz mais próxima encontrada foi", chosen)

