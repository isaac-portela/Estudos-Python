# Isaac Portela da Silva
# matriculate: 20192004900
entrada = [int(i) for i in input().split(" ")]
N, I, F = entrada
vetor = [int(i) for i in input().split(" ")]
aux = []
cont = 0
for i in range(N-1):
    aux.append(vetor[i])
    for j in aux:
        if I <= vetor[i + 1] + j <= F:
            cont += 1
print(cont)