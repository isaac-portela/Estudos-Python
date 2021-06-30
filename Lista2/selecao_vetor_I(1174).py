# Isaac Portela da Silva
# matriculate: 20192004900
a = []
for i in range(100):
    a.append(float(input()))
for n in range(len(a)):
    if a[n] <=10:
        print("A[{}] = {:.1f}".format(n, a[n]))
