# Isaac Portela da Silva
# matriculate: 20192004900
from math import prod
c = int(input())
for i in range(c):
    vet = []
    multi = 1
    str = 'k'
    cadeia_char = input()
    cadeia_char = cadeia_char.split('k')
    for j in range(len(cadeia_char)):
        multi *= cadeia_char[j].count('a')
    for a in range(multi):
        str += 'a'
    print(str)
