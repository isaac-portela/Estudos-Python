'''
PROBLEMA
1152: Estradas Escuras
NOME - MATRICULA
Isaac Portela da Silva - 20192004900
Mateus Leal Sobreira - 20192020340
Mayara do Carmo Mendes - 20192004768

DESCRICAO
Para determinar  quantidade máxima de dinheiro que o governo de Byteland economizara não iluminando algumas ruas, utilizamos o algoritmo de kruskal, que ira ordenar todas 
as arestas do grafo em ordem  crescente, após isso ele ira verificar nesta ordem feita acima se os vértices u e v pertencem ao mesmo conjunto. Caso não pertençam ao mesmo
conjunto ele une esse vértices de modo com que ele crie um subconjunto que inclui todos os vértices dos grafo, formando uma arvore geradora minimima, onde a soma dos 
pesos das arestas dessa arvore e a menor possível. Assim ao terminar de executar o algoritmo de kruskal teremos o menor valor que o governo gastaria com a iluminação
de algum caminhos de qualquer junção da cidade para outra junção, já que para iluminar o metro de estrada custa 1 dólar. Assim para encontrar o valor que o governo
economizaria não iluminando algumas ruas, basta fazermos a diferença do valor total gasto antes para iluminar cada metro de rua pelo valor que o governo está gastando após
implementação do plano de redução de custos.
'''

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
    uf = UnionFind(num_v)
    arestas.sort()
    custo = 0
    for peso, u, v in arestas:
        if uf.union(u, v):
            custo += peso
    return custo

while True:
    n_vertices, n_caminhos = map(int, input().split())

    if n_vertices == 0 and n_caminhos == 0:
        break

    grafo = []
    dolares_gastados_ant = 0
    for i in range(n_caminhos):
        u, v, peso = map(int, input().split())
        grafo.append((peso, u, v))
        grafo.append((peso, v, u))
        dolares_gastados_ant += peso

    dolares_gastada_apos_economizar = kruskal(grafo, n_vertices)
    print(dolares_gastados_ant - dolares_gastada_apos_economizar)