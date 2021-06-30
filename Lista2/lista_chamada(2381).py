# Isaac Portela da Silva
# matriculate: 20192004900
x = map(int, input().split())
n , k = x
lista = []
for i in range(n):
    lista.append(input())

lista = sorted(lista)

for j in range(len(lista)):
    if k-1 == j:
        print(lista[j])