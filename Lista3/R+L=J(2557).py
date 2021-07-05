# Isaac Portela da Silva
# matriculate: 20192004900

while True:
    try:
        entrada = input()
        entrada = entrada.replace('+', '=')
        entrada = entrada.split('=')
        if entrada[0].isdigit() == False :
            result = int(entrada[2]) - int(entrada[1])

        elif entrada[1].isdigit() == False :
            result = int(entrada[2]) - int(entrada[0])

        elif entrada[2].isdigit() == False :
            result = int(entrada[0]) + int(entrada[1])

        print(result)
    except EOFError:
        break
