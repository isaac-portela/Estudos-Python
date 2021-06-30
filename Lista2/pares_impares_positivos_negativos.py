# Isaac Portela da Silva
# matriculate: 20192004900
par = impar = positivo = negativo = 0
i = 0
while i < 5:
    num = int(input())
    if (num % 2) == 0:
        par += 1
    else:
        impar += 1
    if num > 0:
        positivo += 1
    elif num < 0:
        negativo += 1
    i += 1

print(par, "valor(es) par(es)")
print(impar, "valor(es) impar(es)")
print(positivo, "valor(es) positivo(s)")
print(negativo, "valor(es) negativo(s)")
