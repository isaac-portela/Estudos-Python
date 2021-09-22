import math

from heapq import heappush, heappop

def prim(g, num_v):
    v1 = 0      #veritice inicial a ser inserido
    custo = 0
    inserido = [False]*(num_v) #vertices inseridos na arvore
    num_a_inseridos = 0
    pq = [] #fila de prioridade

    #processa vertice inicial
    inserido[v1] = True
    for v2, peso in g[v1]:
        if not inserido[v2]:
            heappush(pq, (peso, v1, v2))

    while pq:
        peso, v1, v2 = heappop(pq)
        if not inserido[v2]:
            inserido[v2] = True
            num_a_inseridos += 1
            custo += peso
            for v3, peso in g[v2]:
                if not inserido[v3]:
                    heappush(pq, (peso, v2, v3))
        if num_a_inseridos == num_v-1:
            break
    return custo/100

c = int(input())
for i in range(c):
    n = int(input())
    arestas = []
    grafo = [[] for i in range(n+1)]
    for i in range(n):
        x, y = map(int, input().split())
        arestas.append((x, y))
    for i in range(len(arestas)):
        for j in range(i+1, len(arestas)):
            distancia = math.sqrt(math.pow(arestas[j][0] - arestas[i][0], 2) + math.pow(arestas[j][1] - arestas[i][1], 2))
            grafo[i].append([j, distancia])
            grafo[j].append([i, distancia])
    minimo_teia = prim(grafo, n)

    print("{:.2f}".format(minimo_teia))