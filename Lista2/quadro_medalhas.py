# Isaac Portela da Silva
# matriculate: 20192004900
ordem = dict()
aux = dict()
n = int(input())
for i in range(n):
    x = input().split()
    pais = str(x[0])
    x = [int(x[k]) for k in range(1, len(x))]
    ordem[pais] = x[:]
for k in sorted(ordem):
    aux[k] = ordem[k]

for j in sorted(aux, key=aux.get, reverse=True):
    print(j, " ".join(map(str, aux[j])))


