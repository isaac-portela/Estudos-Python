# Isaac Portela da Silva
# matriculate: 20192004900
teste = 0
while True:
    N = int(input())
    if N == 0:
        break
    nome1 = input()
    nome2 = input()
    teste += 1
    print("Teste", teste)
    for i in range(N):
        x = map(int, input().split())
        a, b = x

        if (a+b) % 2 == 0:
            print(nome1)
        else:
            print(nome2)
    print()