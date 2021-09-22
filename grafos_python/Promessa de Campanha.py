'''
PROBLEMA
1835: Promessa de Campanha
NOME - MATRICULA
Isaac Portela da Silva - 20192004900
Mateus Leal Sobreira - 20192020340
Mayara do Carmo Mendes - 20192004768

DESCRICAO
Para determinar a quantidade de estradas a serem construídas, utilizamos a DFS  (busca em profundidade). Assim caso ha um caminhos entre os vértices u e v
verificamos se não foi visitado, caso isso ocorra visitamos o vértice e todos os seus vizinhos e mudamos o status dos vértices visitados para true.
Assim para cada vértice do grafo testamos se ele não foi visitado, caso verdadeiro chamamos a função "dfs_iterativa(grafo, vertice, visitados)" e como dito acima ela
visitara o vértice e todos os seus vizinhos, isso representará as estradas já construídas. Para cada chamada da DFS determinaremos um componente conexo no programa eles
serão conhecidos como a interconexão dos principais pontos da cidade a partir das estradas.
Assim caso tenhamos apenas 1 componente conexo isso quer dizer que todos os pontos principais da cidade estão interconectados por estradas a promessa do prefeito já foi
cumprida. Caso a resposta seja maior ou igual a 2 componentes conexos, ainda faltam estradas para serem construídas, e a quantidade delas serão determinadas a partir do
valor de  componentes conexos menos um.
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
t = int(input())
caso = 0
for i in range(t):
    caso += 1
    entrada = input()
    if ' ' not in str(entrada):
        n_pt_cidade = int(entrada)
        n_est_contruidas = int(input())
    else:
        n_pt_cidade, n_est_contruidas  = map(int, entrada.split())

    grafo = [[] for j in range(n_pt_cidade+1)]
    visitados = [False] * (n_pt_cidade + 1)
    for i in range(n_est_contruidas):
        u, v = map(int, input().split())
        grafo[u].append(v)
        grafo[v].append(u)

    pontos_interconetados = 0

    for vertice in range(1, n_pt_cidade + 1):
        if not visitados[vertice]:
            dfs_iterativa(grafo, vertice, visitados)
            pontos_interconetados += 1

    if pontos_interconetados - 1 == 0:
        print("Caso #{}: a promessa foi cumprida".format(caso))
    else:
        print("Caso #{}: ainda falta(m) {} estrada(s)".format(caso, pontos_interconetados - 1))
