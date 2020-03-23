nome = input("Digite seu nome: ")
print("Primeiro: {}".format(nome.split()[0]))
posi= len(nome.split())
print("Ultimo: {}".format(nome.split()[posi-1]))