# Considere um grid em que algumas celulas podem ser visitadas (marcada por '.') e
# outras nao (marcada por '#'), como em um labirinto. Para uma dada celula, pode-se
# tentar visitar as quatro celulas vizinhas, exceto para aquelas de limite, que
# possui menos vizinhos.
# Nessa implementacao, usa-se o proprio grid para marcar como celulas visitas com 'X'.
# entrada: grafo3.in

def dfs_grid(grid, i, j, marca='X', livre='.'):
    altura = len(grid)
    largura = len(grid[0])
    para_visitar = [(i, j)]
    grid[i][j] = marca
    while para_visitar:
        i1, j1 = para_visitar.pop()
        for i2, j2 in [(i1 + 1, j1), (i1, j1 + 1), (i1 - 1, j1), (i1, j1 - 1)]:
             if (0 <= i2 < altura and 0 <= j2 < largura and grid[i2][j2] == livre):
                 grid[i2][j2] = marca # marca o caminho
                 para_visitar.append((i2, j2))

# le grid
altura, largura = map(int, input().split())
grid = [list(input()) for i in range(altura)]

for l in grid:
    print(l)

print()

dfs_grid(grid, 0, 0)

for l in grid:
    print(l)