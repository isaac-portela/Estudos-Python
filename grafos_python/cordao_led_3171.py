'''
PROBLEMA
3171:Cordão de Led

NOME - MATRICULA
Isaac Portela da Silva - 20192004900
Mateus Leal Sobreira - 20192020340
Mayara do Carmo Mendes - 20192004768

DESCRICAO
Para verificar se todos os cordões de leds estão unidos, é usada a DFS 
(busca em profundidade). Assim caso haja um caminhos entre os vértices u e v 
verificamos se não foi visitado, caso isso ocorra visitamos o vértice e todos 
os seus vizinhos e armazenamos os vértices visitados em conjuntos para garantir 
que não serão armazenados vértices repetidos.
Após isso basta verificar se  o  último led pertence ao conjuntos visitados, 
caso verdadeiro, o último led está interconectado com os outros, assim o led 
está completo. Caso contrário o led estará incompleto.

'''


def dfs_iterativa(grafo, vertice_fonte):
    visitados = set()
    visitados.add(vertice_fonte)
    falta_visitar = [vertice_fonte]
    while falta_visitar:
        vertice = falta_visitar.pop()

        for vizinho in grafo[vertice - 1]:
            if vizinho not in visitados:
                visitados.add(vizinho)

                falta_visitar.append(vizinho)
    return visitados


n, l = map(int, input().split())
grafo = [[] for i in range(n)]
for i in range(l):
    u, v = map(int, input().split())
    grafo[u-1].append(v)
    grafo[v-1].append(u)
visitados = dfs_iterativa(grafo, 1)

if n in visitados: 
    print("COMPLETO") 
else: 
    print("INCOMPLETO")