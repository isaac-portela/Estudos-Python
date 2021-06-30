# Isaac Portela da Silva
# matriculate: 20192004900
bit = [50, 10, 5, 1]
resul = [0, 0, 0, 0]
v = 5
cont = 0
while True:
    v = int(input())
    if v == 0:
        break
    cont += 1
    for i in range(4):
        resul[i] = v / bit[i]
        v = v % bit[i]
    resul = [int(x) for x in resul]
    print("Teste", cont)
    print(' '.join(map(str, resul)))
    print()
