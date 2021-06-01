import math
valores = input().split(" ")
a, b, c = valores
a = float(a)
b = float(b)
c = float(c)
delta = (b**2) - (4 * a * c)
if a != 0 and delta > 0:
    r1 = (-b + math.sqrt(delta)) / (2 * a)
    r2 = (-b - math.sqrt(delta)) / (2 * a)
    print('R1 = {:.5f}'.format(r1))
    print('R2 = {:.5f}'.format(r2))
else:
    print("Impossivel calcular")
