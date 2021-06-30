# Isaac Portela da Silva
# matriculate: 20192004900
def fib(n):
    v = [0, 1]
    if n > 1:
        for i in range(2, n + 1):
            f = v[i-2] + v[i-1]
            v.append(f)

    return v[n]

t = int(input())

for i in range(t):
    n = int(input())
    f = fib(n)
    print("Fib({}) = {}".format(n, f))