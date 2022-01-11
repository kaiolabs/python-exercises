from collections import Counter ## O Counter ele aje como um dicionário e pode ser inicializado com uma lista.

listNumeros = list()
dicionarioNumeros = dict()

while True:
    
    numEntrada = str(input("Digite um número:"))
    numero = int(numEntrada)

    if numero <= 0:
        break
    else:
        listNumeros.append(numEntrada)

dicionarioNumeros = Counter(ns[0] for ns in listNumeros)

print("\n")

for repnumeros in dicionarioNumeros:
    chave = repnumeros
    valor = dicionarioNumeros[repnumeros]
    print("O número {} se repete {} vezes.".format(chave, valor))

print("\n")