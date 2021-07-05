"""
    - Isaac Portela da Silva
    - 20192004900
"""


def print_espiral(matriz, n):
    for i in range(n):
        for j in range(n):
            print(matriz[i][j], end='')
        print()
    print("@")


def espiralquadrada(matriz, n):
    cordenadas = ['>', '^', '<', 'v', '>>']
    cont = 0
    linha = coluna = round(n/2 - 0.5)

    while cont != round(n/2 - 0.5):
        for i in range(5):
            if cordenadas[i] == '>':
                matriz[linha][coluna] = 'O'
                coluna += 1
                matriz[linha][coluna] = 'X'
                print_espiral(matriz,n)

            elif cordenadas[i] == '^':
                for k in range(2*cont+1):
                    matriz[linha][coluna] = 'O'
                    linha -= 1
                    matriz[linha][coluna] = 'X'
                    print_espiral(matriz,n)
                
            elif cordenadas[i] == '<':
                for k in range(2*(cont+1)):
                    matriz[linha][coluna] = 'O'
                    coluna -= 1
                    matriz[linha][coluna] = 'X'
                    print_espiral(matriz,n)

            elif cordenadas[i] == 'v':
                for k in range(2*(cont+1)):
                    matriz[linha][coluna] = 'O'
                    linha += 1
                    matriz[linha][coluna] = 'X'
                    print_espiral(matriz,n)

            elif cordenadas[i] == '>>':
                for k in range(2*(cont+1)):
                    matriz[linha][coluna] = 'O'
                    coluna += 1
                    matriz[linha][coluna] = 'X'
                    print_espiral(matriz,n)

        cont += 1


while True:
    n = int(input())
    if n == 0:
        break

    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            if i == j == round(n/2 - 0.5):
                linha.append('X')
            else:
                linha.append('O')

        matriz.append(linha)

    print_espiral(matriz, n)
    espiralquadrada(matriz, n)
