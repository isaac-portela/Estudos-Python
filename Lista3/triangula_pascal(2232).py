# Isaac Portela da Silva
# matriculate: 20192004900
import math
t = int(input())
for i in range(t):
    n = int(input())
    resul = 0
    for j in range(n):
        resul += math.pow(2, j)
    print(int(resul))