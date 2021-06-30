# Isaac Portela da Silva
# matriculate: 20192004900
import math
teste = 0
while True:
    n = int(input())
    if(n == -1):
        break
    teste += 1
    result = (1 + math.pow(2, n)) * (1 + math.pow(2, n))
    print("Teste", teste)
    print(int(result))
    print()
