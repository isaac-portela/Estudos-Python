# Isaac Portela da Silva
# matriculate: 20192004900
while True:
    n = int(input())
    if n == 0:
        break
    matriz = []
    for i in range(n):
        linha = []
        aux = 0
        for j in range(n):
            if i == 0:
                linha.append(j+1)
            else:
                if i-j >= 0:
                    linha.append(matriz[0][i-j])
                else:
                    aux += 1
                    linha.append(matriz[0][aux])
        matriz.append(linha)

    for i in range(n):
        for j in range(n):
            if j == 0:
                print('{:>3}'.format(matriz[i][j]), end="")
            else:
                print('{:>4}'.format(matriz[i][j]), end="")
        print()
    print()

