# Isaac Portela da Silva
# matriculate: 20192004900
N = []
aux = 0
for i in range(20):
    x = int(input())
    N.append(x)
vetor = N[::-1]
for k in vetor:
    print('N[{}] = {}'.format(aux, k))
    aux += 1