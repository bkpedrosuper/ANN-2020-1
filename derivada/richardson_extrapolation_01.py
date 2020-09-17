import math

hs = [.1,.05,.025,.0125]

for h in hs:
    def f(x):
        return math.exp(-x**2)
    n = 4 # ordem do erro
    x0 = 1
    p = 1
    
    print("para h igual a", h)

    def F1(h):
        # return (f(p)-f(p-h))/h
        # return (f(p+h)-f(p-h))/(2*h)
        return (f(p-2*h)-8*f(p-h)+8*f(p+h)-f(p+2*h))/(12*h)

    print('aprox2:', F1(h))

    def Fk(h, n, p):
        # I'm recursive :)
        if n == 1:
            return F1(h)
        n -= 1
        return (2 ** (n * p) * Fk(h/2, n, p) - Fk(h, n, p)) / (2 ** (n * p) - 1)

    print(f'aprox{n}:', Fk(h, n, p))

    # import sympy as sy

    # x = sy.Symbol('x')
    # f = sy.sympify('cos(x**x)')
    # df = sy.diff(f, x, 2).subs(x, x0).evalf()
    # print('exact:', df)
