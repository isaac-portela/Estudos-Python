n = int(input())
n_init = n
n_cel100 = 0
n_cel50 = 0
n_cel20 = 0
n_cel10 = 0
n_cel5 = 0
n_cel2 = 0
n_cel1 = 0
if n % 100 != n:
    n_cel100 = (n - (n % 100)) / 100
    n = n % 100
if n % 50 != n:
    n_cel50 = (n - (n % 50)) / 50
    n = n % 50
if n % 20 != n:
    n_cel20 = (n - (n % 20)) / 20
    n = n % 20
if n % 10 != n:
    n_cel10 = (n - (n % 10)) / 10
    n = n % 10
if n % 5 != n:
    n_cel5 = (n - (n % 5)) / 5
    n = n % 5
if n % 2 != n:
    n_cel2 = (n - (n % 2)) / 2
    n = n % 2
if n % 1 != n:
    n_cel1 = (n - (n % 1)) / 1
    n = n % 1

print(n_init)
print(int(n_cel100), 'nota(s) de R$ 100,00')
print(int(n_cel50), 'nota(s) de R$ 50,00')
print(int(n_cel20), 'nota(s) de R$ 20,00')
print(int(n_cel10), 'nota(s) de R$ 10,00')
print(int(n_cel5), 'nota(s) de R$ 5,00')
print(int(n_cel2), 'nota(s) de R$ 2,00')
print(int(n_cel1), 'nota(s) de R$ 1,00')
