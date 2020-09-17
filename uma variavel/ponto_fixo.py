# seja g:[a,b]->R
# 0. g tem que ser contínua
# 1. g(x)\in [a,b] para todo x\in[a,b] é o mesmo que g([a, b])\subset[a,b]
# 2. |g'(x)| < 1 para todo x\in[a,b]
# f(x) = 0 <--> g(x) = x
import math
def g(x):
    return (math.sin(x)+4)/2

a, b = [2,3]
x0 = 2.72
n=10
print("Realizando o método com",n,"iterações")
print("O intervalo escolhido foi [", a, ",", b, "]")
for i in range(n):
    xn = g(x0)
    x0 = xn
    print(i, x0)
print("Melhor aproximação encontrada:", x0)
