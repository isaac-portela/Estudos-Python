'''
PROBLEMA
1855: Mapa do Meistre
NOME - MATRICULA
Isaac Portela da Silva - 20192004900
Mateus Leal Sobreira - 20192020340
Mayara do Carmo Mendes - 20192004768

DESCRICAO
Para verificar se o mapa leva  ou não a um ponto com um baú de obsidiana, utilizamos um grafo para armazenar todos os elementos do mapa. Começamos a fazer a busca
a partir da posição [0][0] do mapa, verificamos qual caractere está contido nesse posição de modo a determinar qual a primeira direção que vamos seguir.
Dado essa posição incrementamos ou decrementos o valor dos eixos X ou Y, de modo a percorrer o mapa salvando as posições já visitadas e verificando se estamos mudando de direção ou não,
até chegar no caractere "*" que indica que encontremos o baú e portanto o mapa e valido ou até ocorrer de  não encontremos o baú no mapa ou caso sejamos mandados
para fora dele, oque significa que o mapa é inválido.
'''

def qualdirec(direcao,x, y):
    if direcao == '>':
        x += 1
    elif direcao == '<':
        x -= 1
    elif direcao == 'v':
        y += 1
    elif direcao == '^':
        y -= 1
    return x, y

l = int(input())
h = int(input())
mapa = [[] for i in range(h)]
visitados = [[False]*l for i in range(h)]
for i in range(h):
    mapa[i] = list(input())
direcao = ''
x, y = 0, 0
while(x!=-1 and y!=-1 and x<l and y<h):
        if mapa[y][x] == '*':
            print("*")
            break
        elif mapa[y][x] == '>':
            direcao = '>'
            x += 1
        elif mapa[y][x] == '<':
            direcao = '<'
            x -= 1
        elif mapa[y][x] == 'v':
            direcao = 'v'
            y += 1
        elif mapa[y][x] == '^':
            direcao = '^'
            y -= 1
        elif mapa[y][x] == '.':
            x, y = qualdirec(direcao, x, y)
        if visitados[y][x]:
            print("!")
            break
        visitados[0][0] = True
        visitados[y][x] = True