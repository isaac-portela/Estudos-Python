# Isaac Portela da Silva
# matriculate: 20192004900
x = []
for i in range(10):
    n = int(input())
    if n <= 0:
        n = 1
    x.append(n)

for n in range(len(x)):
    print("X[{}] = {}".format(n,x[n]))

