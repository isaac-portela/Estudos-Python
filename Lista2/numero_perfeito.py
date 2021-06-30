# Isaac Portela da Silva
# matriculate: 20192004900
n = int(input())
divisores = []
for i in range(n):
    x = int(input())
    for v in range(1,x):
        if x % v == 0:
            divisores.append(v)
    if sum(map(int, divisores)) == x:
        print(x, "eh perfeito")
    else:
        print(x, "nao eh perfeito")
    divisores.clear()