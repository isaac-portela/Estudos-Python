# Isaac Portela da Silva
# matriculate: 20192004900
entrada = input().split()
x, y = entrada
while True:
    if(x == y):
        break
    else:
        if int(x) > int(y):
            print("Decrescente")
        else:
            print("Crescente")
    entrada = input().split()
    x, y = entrada


