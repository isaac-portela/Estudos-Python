#busca em largura em grafo direcionado
# entrada: grafo1.in

#recursivo

#apenas visita
def dfs_rec(g, u, visitados):
    visitados[u] = True
    for v in g[u]:
        if not visitados[v]:
            dfs_rec(g, v, visitados)


#iterativo
#prefira este: evita empilhamento recursivo
 
#apenas visita
def dfs_iter1(g, u, visitados):
    vertices_visitar = [u]
    while vertices_visitar:
        u = vertices_visitar.pop()
        if not visitados[u]:
            visitados[u] = True
            for v in g[u]:
                if not visitados[v]:
                    vertices_visitar.append(v)

#visita, registra anterior e ordem de descoberta
def dfs_iter2(g, u, anterior, ordem):
    tempo = 0
    vertices_visitar = [[u, u]] #[vertice, anterior]
    while vertices_visitar:
        u, a = vertices_visitar.pop() #[vertice, anterior]
        if anterior[u] == -1:
            tempo += 1

            anterior[u] = a
            ordem[u] = tempo

            for v in g[u]:
                if anterior[v] == -1:
                    vertices_visitar.append([v, u])

#solucao

#le grafo
num_v, num_a = map(int, input().split())
g = [[] for i in range(num_v+1)]
for i in range(num_a):
    u, v = map(int, input().split())
    g[u].append(v)

#busca em profundidade a partir do vertice 1
u = 1

#recursivo
visitados = [False]*(num_v+1)

dfs_rec(g, u, visitados)

print(visitados)


#iterativo
visitados = [False]*(num_v+1)

dfs_iter1(g, u, visitados)

print(visitados)

#iterativo com mais informacoes
anterior = [-1]*(num_v+1)
ordem = [-1]*(num_v+1)
d = 1

dfs_iter2(g, u, anterior, ordem)

print(anterior)
print(ordem)