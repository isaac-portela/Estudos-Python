# Isaac Portela da Silva
# matriculate: 20192004900
while True:
    try:
        cont = 0
        n = int(input())
        total = {}
        for i in range(n):
            peca = input().split()
            total[peca[0]] = int(peca[1])
        # ordenar o dicionario
        for val in sorted(total, key=total.get):
            cont += 1
            if cont == n:
              print(val)
            else:
                print(val, end=" ")
    except EOFError:
        break