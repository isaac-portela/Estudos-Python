"""
    - Isaac Portela da Silva
    - 20192004900
"""
import math
PI = 3.141592654

while True:
    try:
        entrada = [float(i) for i in input().split(" ")]
        a, b, c = entrada
        angulo = math.tan((a * PI) / 180.0)
        altura = b * angulo
        qtd = (altura + c) * 5
        print("{:.2f}".format(qtd))
    except EOFError:
        break