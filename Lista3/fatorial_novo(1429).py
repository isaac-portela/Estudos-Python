# Isaac Portela da Silva
# matriculate: 20192004900
import math

while True:
    acm = input()
    resultado = 0

    if acm == '0':
        break

    acm = reversed(acm)
    for key, valor in enumerate(acm):
        resultado += int(valor) * int(math.factorial(key + 1))
    print(resultado)
