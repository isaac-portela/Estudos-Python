# Isaac Portela da Silva
# matriculate: 20192004900

teste = 0
while True:
    n = int(input())
    if(n == 0):
        break
    teste += 1
    x = input().split()
    x = [int(i) for i in x]

    for j in range(n):
        if x[j] == (j+1):
            print("Teste", teste)
            print(x[j])
            print()