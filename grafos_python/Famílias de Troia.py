'''
PROBLEMA
2440: Famílias de Troia
NOME - MATRICULA
Isaac Portela da Silva - 20192004900
Mateus Leal Sobreira - 20192020340
Mayara do Carmo Mendes - 20192004768

DESCRICAO
Para determinar a quantidade de famílias distintas que aparece no grafo, utilizamos a DFS  (busca em profundidade). Assim caso haja um caminhos entre os vértices u e v
verificamos se não foi visitado, caso isso ocorra visitamos o vértice e todos os seus vizinhos e mudamos o status dos vértices visitados para true.
Assim para cada vértice do grafo testamos se ele não foi visitado, caso verdadeiro chamamos a função "dfs_iterativa(grafo, vertice, visitados)" e como dito acima ela
visitara o vértice e todos os seus vizinhos, isso representara uma família. Como cada chamada função DFS que ira definir uma família distinta. Basta a cada vez que está função for chamada
incrementarmos a variável "familia" em uma unidade. Assim no fim teremos a quantidade de famílias distintas.
'''

def dfs_iterativa(grafo, vertice_fonte, visitados):
    visitados[vertice_fonte] = True
    falta_visitar = [vertice_fonte]
    while falta_visitar:
        vertice = falta_visitar.pop()
        for vizinho in grafo[vertice]:
            if not visitados[vizinho]:
                visitados[vizinho] = True
                falta_visitar.append(vizinho)


n_vertices, n_arestas = map(int, input().split())

grafo = [[] for i in range(n_vertices+1)]
visitados = [False] * (n_vertices+1)

for i in range(n_arestas):
    u, v = map(int, input().split())
    grafo[u].append(v)
    grafo[v].append(u)

familias = 0
for vertice in range(1, n_vertices+1):
    if not visitados[vertice]:
      dfs_iterativa(grafo, vertice, visitados)
      familias += 1

print(familias)