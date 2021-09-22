# entrada: grafo5.in

class UnionFind:
    def __init__(self, n):
        self.up_bound = list(range(n)) #vertice representante do componente
        self.rank = [0]*n              #ranking no representante
    
    def find(self, x_index):
        if self.up_bound[x_index] == x_index:
            return x_index
        
        self.up_bound[x_index] = self.find(self.up_bound[x_index])
        return self.up_bound[x_index]
    
    def union(self, x_index, y_index):
        repr_x = self.find(x_index)
        repr_y = self.find(y_index)

        if repr_x == repr_y: #ja estao no mesmo componente
            return False
        
        if self.rank[repr_x] == self.rank[repr_y]:
            self.rank[repr_x] += 1
            self.up_bound[repr_y] = repr_x
        elif self.rank[repr_x] > self.rank[repr_y]:
            self.up_bound[repr_y] = repr_x
        else:
            self.up_bound[repr_x] = repr_y
        
        return True


def kruskal(arestas, num_v):
    uf = UnionFind(num_v+1)
    arestas.sort()
    agm = []
    custo = 0
    for peso, u, v in arestas:
        if uf.union(u, v):
            agm.append((u, v))
            custo += peso
    return agm, custo

#le grafo como lista de arestas
num_v, num_a = map(int, input().split())
arestas = []

for i in range(num_a):
    u, v, peso = map(int, input().split())
    arestas.append((peso, u, v))

agm, custo = kruskal(arestas, num_v)

print(agm)
print(custo)