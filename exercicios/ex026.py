frase = input("Digite uma frase: ").strip().upper()
print("Na frase tem {} A".format(frase.count("A")))
print("Em sua primeira vez a palavra A aparece na posição[{}]".format(frase.find("A")+1))
print("A ultima vez a palavra A aparece na posição[{}]".format(frase.rfind("A")+1))   