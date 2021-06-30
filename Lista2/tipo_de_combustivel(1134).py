# Isaac Portela da Silva
# matriculate: 20192004900
tipos = {1: "Alcool", 2: "Gasolina", 3:"Diesel"}
resultado = {'Alcool': 0, 'Gasolina': 0, 'Diesel': 0}
tipo = 0
while(tipo != 4):
    tipo = int(input())
    if tipo in tipos.keys():
        resultado[tipos[tipo]] += 1

print("MUITO OBRIGADO")
print("Alcool:", resultado['Alcool'])
print("Gasolina:", resultado['Gasolina'])
print("Diesel:", resultado['Diesel'])