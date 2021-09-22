def dfs_iterativa(grafo, vertice_fonte):
    cont = 0
    falta_visitar = vertice_fonte
    while True:
        try:
            x = grafo[falta_visitar][0]
            cont += 1
            grafo[falta_visitar][0] = -1
            if x == 1:
                break
            if x == -1 and falta_visitar != 1:
                cont = 0
                break
            falta_visitar = x
        except:
            break
    return cont

n = int(input())
grafo = [[] for i in range(n+1)]
for i in range(n):
    u, v = map(int, input().split())
    grafo[u].append(v)

r = dfs_iterativa(grafo, 1)

if r == n:
    print('S')
else:
    print('N')