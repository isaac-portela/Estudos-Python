# Isaac Portela da Silva
# matriculate: 20192004900
teste = 0
while True:
    n = int(input())
    if n == 0:
        break
    diferenca = 0
    teste += 1
    j = z = 0
    print("Teste", teste)
    for i in range(n):
        entrada = input().split(" ")
        j, z = entrada
        diferenca = (int(j) - int(z)) + diferenca
        print(diferenca)
    print()
