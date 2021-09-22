#busca em largura
# entrada: grafo1.in

from collections import deque

def bfs(g, u, anterior, distancia):
    para_visitar = deque()
    distancia[u] = 0
    anterior[u] = u
    para_visitar.appendleft(u)

    while para_visitar:
        u = para_visitar.pop()
        for v in g[u]:
            if distancia[v] == float('inf'):
                distancia[v] = distancia[u] + 1
                anterior[v] = u
                para_visitar.appendleft(v)
    
    return distancia, anterior


#solucao

#le grafo
num_v, num_a = map(int, input().split())
g = [[] for i in range(num_v+1)]
for i in range(num_a):
    u, v = map(int, input().split())
    g[u].append(v)

#busca em largura a partir do vertice 1
u = 1

anterior = [-1]*(num_v+1)
distancia = [float('inf')]*(num_v+1)

d, a = bfs(g, u, anterior, distancia)

print(anterior)
print(distancia)