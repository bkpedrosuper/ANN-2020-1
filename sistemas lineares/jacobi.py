# E = [[9,1,1,3,6], [2,7,2,1,3], [1,2,6,1, 11], [1,1,1,19,0]] # matrix estendida do sistema
E = [[4,1,1,6], [2,5,2,3], [1,2,4,11]] # matrix estendida do sistema
# 4x+y+z=6 --> x = (6 - y - z) / 4
# 2x+5y+2z=3 --> y = (3 - 2x - 2z) / 5
# x+2y+4z=11 --> z = (11 - x - 2y) / 4

def test(matrix, vec):
    err = []
    for row in matrix:
        prod = abs(sum([col * vec for col, vec in zip(row[:-1], vec)]) - row[-1])
        err.append(prod)
    return err

row = 3
col = 4

n  = 4
itr = {}
# chute = [0,0,0,1]
xn = []
chute = [0,0,1]
print("Resolvendo o sistema abaixo:")
print ("{")
for i in range(row):
    for j in range(col):
        if(j==row):
            print(" = ", E[i][j])
        else:
            print (E[i][j], " ", end="")
print("}\n")
print("chute inicial: [")
print("x","y","z")
print(*chute)
print("]\n")
print("Número de iterações usado:",n)
for i in range(n):
    xn = []
    for j, row in enumerate(E):
        subs = sum([el * chute[k] for k, el in enumerate(row[:-1]) if k != j])
        subs = (row[-1] - subs) / row[j]
        xn.append(subs)
    chute = xn
    print(i,xn)
print("\nSolução:",xn)
