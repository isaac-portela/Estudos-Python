# Isaac Portela da Silva
# matriculate: 20192004900
n1 = 0
n2 = 1
cont = 2
fib = [n1, n2]
n = int(input())
while n > cont:
    n3 = n1 + n2
    fib.append(n3)
    cont += 1
    n1, n2, = n2, n3

print(' '.join(map(str, fib)))

