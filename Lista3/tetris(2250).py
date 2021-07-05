# Isaac Portela da Silva
# matriculate: 20192004900
teste = 0
while True:
    n = int(input())
    if n == 0:
        break
    dicionario = dict()
    aux = dict()
    teste += 1
    for i in range(n):
        nome = input()
        pontuacoes = [int(n) for n in input().split(" ")]
        pontuacoes = sorted(pontuacoes)
        dicionario[nome] = pontuacoes[1:11]

    for key in dicionario:
        dicionario[key] = sum(dicionario[key])

    for k in sorted(dicionario):
        aux[k] = dicionario[k]
    cont = 0
    ant = -1
    cont_n = 0
    print("Teste", teste)
    for j in sorted(aux, key=aux.get, reverse=True):
        cont_n += 1
        if ant == -1:
            cont += 1
            print("{} {} {}".format(cont, aux[j], j))
            ant = aux[j]
        elif ant == aux[j]:
            print("{} {} {}".format(cont, aux[j], j))
        else:
            cont = cont_n
            print("{} {} {}".format(cont, aux[j], j))
            ant = aux[j]
    print()