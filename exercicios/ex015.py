aluguelCar = float(input("Quantos dias foram alugados? "))
kmRodados = float(input("Quantos Km rodados? "))
valor = (aluguelCar * 60) + (kmRodados * 0.15)
print("O valor a pagar é de R${:.2f}".format(valor))