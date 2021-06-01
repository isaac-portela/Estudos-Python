n = int(input())
print(n)
cedulas = [100, 50, 20, 10, 5, 2, 1]

for cedula in cedulas:
    n_cel = 0
    if n % cedula != n:
        n_cel = (n - (n % cedula)) / cedula
        n = n % cedula
    print('{} nota(s) de R$ {},00'.format(int(n_cel), cedula))
