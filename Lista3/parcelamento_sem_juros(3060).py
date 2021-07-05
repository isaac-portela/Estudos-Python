# Isaac Portela da Silva
# matriculate: 20192004900
valor = int(input())
parcelas = int(input())
resto = valor % parcelas

if resto == 0:
    vp = int(valor / parcelas)
    for i in range(parcelas):
        print(vp)
else:
    vp = valor / parcelas
    for i in range(resto):
        print(round(vp + 0.5))
    for i in range(parcelas - resto):
        print(round(vp - 0.5))
