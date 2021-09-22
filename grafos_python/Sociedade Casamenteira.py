'''
PROBLEMA
1902:Sociedade Brasileira Casamenteira
NOME - MATRICULA
Isaac Portela da Silva - 20192004900
Mateus Leal Sobreira - 20192020340
Mayara do Carmo Mendes - 20192004768

DESCRICAO
Para verificar a quantidade de casamentos que são possíveis de se formar, é usada a DFS 
(busca em profundidade). Assim caso haja um caminhos entre os vértices u e v 
verificamos se o vértice não foi visitado, caso isso ocorra visitamos o vértice e todos 
os seus vizinhos, mudando os status dos vértices visitados para true, e adicionando os vértices na lista que armazena as pessoas que pertencem ao casamento atual.
Assim fazemos um for para fazer uma varredura de cada vértice do grafo, e caso o vértice verificado na DFS foi visitado, verificamos se este vértice está inserido
na lista que armazena as pessoas do casamento atual, e também se a quantidade de pessoas pertencentes a esse casamento são maior que 2, pois no mínimo o casamento
deve ser formado por duas pessoas. Caso verdadeiro retornamos o numero 1 que indica que temos mais um casamento formado, caso contrario retornamos 0.
Na main incrementamos este valor retornado com o valor da variável comp_conexo, que no fim indicara a quantidade total de casamentos formados.

'''


def dfs_iterativa(grafo, vertice_fonte, visitados):
    pessas_do_casamento = []
    falta_visitar = [vertice_fonte]
    while falta_visitar:
        vertice = falta_visitar.pop()
        if not visitados[vertice]:
            visitados[vertice] = True
            pessas_do_casamento.append(vertice)
            if not visitados[grafo[vertice]]:
                falta_visitar.append(grafo[vertice])
            elif grafo[vertice] in pessas_do_casamento and len(pessas_do_casamento) >= 2: 
                return  1
        else: 
            return 0
    return 0
        
grafo = dict()
teste = 0
visitados = dict()
while True:
  try:
      a, b = map(str, input().split())
      grafo[a] = b
      visitados[a] = False
  except:
    break;
comp_conexo = 0
for vertice in grafo:
      f = dfs_iterativa(grafo, vertice, visitados)
      comp_conexo += f
print(comp_conexo)

