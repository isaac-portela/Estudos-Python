# Isaac Portela da Silva
# matriculate: 20192004900
n = int(input())
menor_preco = 2000000
for i in range(n):
    entrada = input().split(" ")
    p, g = entrada
    menor_preco = min(menor_preco, (float(p) * 1000) / float(g))

print("{:.2f}".format(menor_preco))