# Isaac Portela da Silva
# matriculate: 20192004900
n = int(input())
for i in range(n):
    string_calc = input()
    for c in string_calc:
        if not c.isdigit():
            string_calc = string_calc.replace(c, 'c')
    string_calc = string_calc.split('c')
    soma = 0
    for k in string_calc:
        if k.isdigit():
            soma += int(k)
    print(soma)
