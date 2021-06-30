# Isaac Portela da Silva
# matriculate: 20192004900
n = int(input())
for i in range(n):
    entrada = input().split(" ")
    a, b, c = entrada
    print("{:.1f}".format((float(a) * 2 + float(b) * 3 + float(c) * 5) / 10))
