# Considere um grid em que algumas celulas podem ser visitadas (marcada por '.') e
# outras nao (marcada por '#'), como em um labirinto. Para uma dada celula, pode-se
# tentar visitar as quatro celulas vizinhas, exceto para aquelas de limite, que
# possui menos vizinhos.
# Nessa implementacao, usa-se o proprio grid para marcar como celulas visitas com 'X'.
# entrada: grafo3.in

def bfs_grid(grid,griddist,i, j, altura, largura, marca='#', livre='.'):
    altura = altura
    largura = largura
    para_visitar = [(i, j)]
    griddist[i][j] = 0
    grid[i][j] = marca
    while para_visitar:
        i1, j1 = para_visitar.pop(0)
        for i2, j2 in [(i1 - 1, j1), (i1, j1 - 1), (i1 + 1, j1), (i1, j1 + 1)]:
             if (0 <= i2 < altura and 0 <= j2 < largura and grid[i2][j2] == livre):
                 grid[i2][j2] = marca # marca o caminho
                 para_visitar.append((i2, j2))
                 if(griddist[i2][j2] == float('inf')):
                    griddist[i2][j2] = griddist[i1][j1] + 1
                
                 

# le grid
dist_tot = 0
qtd_po , qnt_mov = map(int, input.split())
altura, largura = map(int, input().split())
grid = []
floco = []
x_r, y_r = 0, 0
x_f, y_f = 0, 0
griddist = [list(float('inf') for v in range(largura)) for i in range(altura)]
for i in range(altura):
    linha = list(input())
    grid.append(linha)
    for indice, dado in enumerate(linha):
        if dado == 'R':
            x_r, y_r = i, indice
        elif dado == '*':
            floco.append((i, indice))
            linha[i][indice] = '.'
        elif dado == 'S':
            x_f , y_f = i, indice
            linha[i][indice] = '.'
        
for i in range(qtd_po + 1):
    bfs_grid(grid,griddist, altura,largura ,x_r, y_r)
    

for l in griddist:
    print(l)

