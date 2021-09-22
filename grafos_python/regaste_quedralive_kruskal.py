'''
PROBLEMA
1552: Resgate em Queda Livre
NOME - MATRICULA
Isaac Portela da Silva - 20192004900
Mateus Leal Sobreira - 20192020340
Mayara do Carmo Mendes - 20192004768

DESCRICAO
Para determinar o comprimento mínimo da teia em metros, primeiro precisamos encontrar a distancia entre cada uma das pessoas com a coordenada (x, y) para todas outras pessoas em
outras coordenadas. Armazenando a distancia da pessoa em um grafo juntamente com vértices u e v. Após isso utilizamos o algoritmo de kruskal, que ira ordenar todas 
as arestas do grafo em ordem  crescente, após isso ele ira verificar nesta ordem feita acima se os vértices u e v pertencem ao mesmo conjunto. Caso não pertençam ao mesmo
conjunto ele une esse vértices de modo com que ele crie um subconjunto que inclui todos os vértices dos grafo, formando uma arvore geradora minimima, onde a soma dos 
pesos das arestas dessa arvore e a menor possível. Assim ao terminar de executar o algoritmo de kruskal teremos o comprimento mínimo da teia do homem aranha em centímetros,
mas como o problema pede a resposta em metros precisamos converter o resultado dividindo por 100.
'''


import math

class UnionFind:
    def __init__(self, n):
        self.up_bound = list(range(n))  # vertice representante do componente
        self.rank = [0] * n  # ranking no representante

    def find(self, x_index):
        if self.up_bound[x_index] == x_index:
            return x_index

        self.up_bound[x_index] = self.find(self.up_bound[x_index])
        return self.up_bound[x_index]

    def union(self, x_index, y_index):
        repr_x = self.find(x_index)
        repr_y = self.find(y_index)

        if repr_x == repr_y:  # ja estao no mesmo componente
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
    uf = UnionFind(num_v)
    arestas.sort()
    custo = 0
    for peso, u, v in arestas:
        if uf.union(u, v):
            custo += peso
    return custo/100

c = int(input())
for i in range(c):
    n = int(input())
    arestas = []
    grafo = []
    for i in range(n):
        x, y = map(int, input().split())
        arestas.append((x, y))
    for i in range(len(arestas)):
        for j in range(i+1, len(arestas)):
            distancia = math.sqrt(math.pow(arestas[j][0] - arestas[i][0], 2) + math.pow(arestas[j][1] - arestas[i][1], 2))
            grafo.append((distancia, i, j))
            grafo.append((distancia, j, i))
    minimo_teia = kruskal(grafo, n)

    print("{:.2f}".format(minimo_teia))