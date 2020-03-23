cidade = input("Digite o nome da sua cidade: ")
posicao = cidade.upper().strip().find("SANTO")
if(posicao==0):
    print("A sua cidade começa com SANTO")
