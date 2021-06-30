# Isaac Portela da Silva
# matriculate: 20192004900
teste = 0
while True:
    temperaturas = []
    media = 0
    anterior = 0
    aux = 0
    entrada = input().split()
    ntm, tamanho = entrada
    ntm = int(ntm)
    tamanho = int(tamanho)
    if ntm == tamanho == 0:
        break
    teste += 1
    for i in range(ntm):
        temperaturas.append(int(input()))

    anterior = sum(temperaturas[:tamanho])
    media = anterior / tamanho
    maior = media
    menor = media
    for i in range(tamanho, len(temperaturas)):
        soma = (anterior - temperaturas[aux]) + temperaturas[i]
        anterior = soma
        media = anterior / tamanho
        if media > maior:
            maior = media
        if media < menor:
            menor = media
        aux += 1

    print("Teste", teste)
    print(int(menor), int(maior))
    print()