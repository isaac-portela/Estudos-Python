# Isaac Portela da Silva
# matriculate: 20192004900
x = int(input())
y = int(input())
if x > y:
    x, y = y, x
for n in range(x+1, y):
    if n % 5 == 2 or n % 5 == 3:
        print(n)