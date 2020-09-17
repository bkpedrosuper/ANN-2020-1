# uma função qualquer
import math

def f(x):
    return x**5-4*x**2+2
    
    # return math.log(x)+x**2

# método da bisseção
i =0
m=0
a, b = [-2, 0]
n = 10 # número de iterações
print("os valores iniciais são: a=", a,"b=",b)
print("O número de iterações é", n)
while(abs(a-b)>0.125):
    m = (a + b) / 2
    if f(m) == 0:
        print('A raiz é:', m)
    elif f(a) * f(m) < 0: # teorema de Bolzano
        b = m
    else:
        a = m
    print(i, m, f(m))
    i+=1
print("A raiz está entre", a, "e", b,". Tamanho do intervalo:", abs(a-b))
print("a raiz mais próxima encontrada foi", m)
