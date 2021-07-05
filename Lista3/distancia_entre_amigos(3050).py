# Isaac Portela da Silva
# matriculate: 20192004900
np = int(input())
predio = [int(i) for i in input().split(' ')]
maior_distancia = 0
cont = 0
posi = 0
for i in range(np):
    d = predio[0] + i + predio[i]
    if d > maior_distancia:
        maior_distancia = d
        posi = i
vet = []
for j in range(np):
    if j != posi:
        dist = predio[posi] + (posi-j) + predio[j]
        vet.append(dist)

print(max(vet))
