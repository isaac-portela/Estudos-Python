# Isaac Portela da Silva
# matriculate: 20192004900
matriz = []
operacao = input()
soma = 0
cont = 0
c = 1
for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)

for i in range(5):
    for j in range(c, 12 - c):
        soma += matriz[i][j]
        cont += 1
    c += 1

if operacao == 'S':
    print("{:.1f}".format(soma))
else:
    print("{:.1f}".format(soma/cont))