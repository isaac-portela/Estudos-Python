# Isaac Portela da Silva
# matriculate: 20192004900
teste = 0
while True:
    n = int(input())
    if n == 0:
        break
    dado = dict()
    teste += 1
    for i in range(n):
        entrada = input().split(" ")
        dado[entrada[0]] = int(entrada[1])

    maior = dado[max(dado, key=dado.get)]
    estagio = [str(key) for key in dado if dado[key] == maior]
    print("Turma", teste)
    print(' '.join(estagio), '')
    print()
