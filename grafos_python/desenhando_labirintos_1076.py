'''
PROBLEMA
1076:Desenhando Labirintos

NOME - MATRICULA
Isaac Portela da Silva - 20192004900
Mateus Leal Sobreira - 20192020340
Mayara do Carmo Mendes - 20192004768

DESCRICAO
Para determinar a quantidade de movimentos que são feitos para desenhar  o labirinto, é usada a DFS
(busca em profundidade). Assim caso haja um caminhos entre os vértices u e v
verificamos se não foi visitado, caso isso ocorra visitamos o vértice e todos
os seus vizinhos e armazenamos os vértices visitados em conjuntos para garantir
que não serão armazenados vértices repetidos.
Para cade vertice visitado a variavel cont e incrementada indicando um movimento do desenho do
labirinto, apos visitado todos os vertices e com o labirinto desenhado totalmente, dobramos o valor de
cont de modo a contabizar os movimentos de retorno ao nodo onde o desenho começou.

'''

def dfs_iterativa(grafo, vertice_fonte):
    cont = 0
    visitados = set()
    visitados.add(vertice_fonte)
    falta_visitar = [vertice_fonte]
    while falta_visitar:
        vertice = falta_visitar.pop()
        for vizinho in grafo[vertice]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                falta_visitar.append(vizinho)
                cont += 1
    return cont


t = int(input())
for i in range(t):
    n = int(input())
    qtd_v, qtd_a = map(int, input().split())
    grafo = [[] for i in range(qtd_v+1)]

    for i in range(qtd_a):
        u, v = map(int, input().split())
        grafo[u].append(v)
        grafo[v].append(u)

    cont = dfs_iterativa(grafo, n)

    print(2 * cont)