# Isaac Portela da Silva
# matriculate: 20192004900

n = 0
cont = 0
media = []
while n!=2:
    n = float(input())
    if 0 <= n <= 10:
        media.insert(cont, n)
        cont += 1
        if cont == 2:
            resultado = (media[0] + media[1]) / 2
            cont = 0
            print("media = {:.2f}".format(resultado))
            print("novo calculo (1-sim 2-nao)")
            while True:
                n = int(input())
                if n == 1 or n == 2:
                    break
                else:
                    print("novo calculo (1-sim 2-nao)")
    else:
        print("nota invalida")
