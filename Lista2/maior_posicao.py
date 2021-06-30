numeros = []
maior = -1
posi = 0
for i in range(100):
    numeros.append(int(input()))

for i in range (len(numeros)):
    if(numeros[i] > maior):
        maior = numeros[i]
        posi = i+1

print(maior)
print(posi)

