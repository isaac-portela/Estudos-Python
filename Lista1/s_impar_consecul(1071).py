x = int(input())
y = int(input())
soma = 0
for n in range(y+1, x):
    if n % 2 != 0:
        soma += n

print(soma)
