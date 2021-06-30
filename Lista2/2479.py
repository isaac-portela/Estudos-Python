# Isaac Portela da Silva
# matriculate: 20192004900
N = int(input())
lista = []
comportaram = 0
for i in range(N):
    c_esp, nome = input().split()
    lista.append(nome)
    if c_esp == '+':
        comportaram += 1
lista.sort()
for j in lista:
    print(j)

print("Se comportaram: {} | Nao se comportaram: {}".format(comportaram, len(lista)-comportaram))