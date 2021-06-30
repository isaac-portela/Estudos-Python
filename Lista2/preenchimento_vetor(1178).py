# Isaac Portela da Silva
# matriculate: 20192004900
x = float(input())
v = []
for i in range(100):
    v.append(x)
    x /= 2
for j in range(len(v)):
    print("N[{}] = {:.4f}".format(j,v[j]))