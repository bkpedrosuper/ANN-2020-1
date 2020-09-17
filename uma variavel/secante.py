# uma função qualquer
import math
def f(x):
    return x**3+x**2 + 0.001

chosen = 0
n = 10
x0, x1 = [0, 2]
itr = {}
itr[0] = x0
itr[1] = x1

a, b = x0, x1
print("O número de iterações é", n)
print("O intervalo escolhido foi [", a, ",", b, "]")
for i in range(n):
    try:
        xn = (a * f(b) - b * f(a)) / (f(b) - f(a)) # a - f(a) / ((f(b) - f(a))/ (b - a))
    except:
        raise ValueError(f"Divisão por zero para {a}, {b} na iteração {i}")
    itr[i + 2] = xn
    print(i, itr[i])
    chosen = itr[i]
    a, b = b, xn

print("a raiz mais próxima encontrada foi", chosen)

