entrada = input().split(" ")
valores = [int(i) for i in entrada]
menor = 2000
maior = -2000
medio = 0
for v in valores:
    if v > maior:
        maior = v
    if v < menor:
        menor = v

for i in valores:
    if maior != i and menor != i:
        medio = i
        break
print(f'{menor}\n{medio}\n{maior}\n')
print(*valores, sep='\n')
