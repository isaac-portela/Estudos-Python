from heapq import heappush, heappop

def prim(g, num_v):
    v1 = 1      #veritice inicial a ser inserido
    agm = []
    custo = 0
    inserido = [False]*(num_v+1) #vertices inseridos na arvore
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
            agm.append((v1, v2))
            custo += peso
            for v3, peso in g[v2]:
                if not inserido[v3]:
                    heappush(pq, (peso, v2, v3))
    return agm, custo


#le grafo
num_v, num_a = map(int, input().split())

g = [[] for i in range(num_v+1)]

for i in range(num_a):
    v1, v2, peso = map(int, input().split())
    g[v1].append([v2, peso])
    g[v2].append([v1, peso])

agm, custo = prim(g, num_v)

print(agm)
print(custo)