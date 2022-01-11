
inventario = {'banana': 50, 'laranja': 12, 'melancia': 7, 'kiwi': 23}

total = 0
for valor in inventario.values():
    total += valor

print("Temos %d frutas no inventario."%(total))
























# listNumeros = [1,1,1,2,3,4,5]

# x = listNumeros.count(1)
# print(x)

# from collections import Counter

# # especie,nome
# listaAnimais = [
#     ('leao', 'Simba'),
#     ('javali', 'Pumba'),
#     ('leao', 'Scar'),
#     ('hiena', 'Banzai'),
#     ('leao', 'Mufasa'),
# ]

# # Criar um contador, o inicializando com a primeira string
# # de cada elemento em `listaAnimais`
# dicEspecies = Counter(animal[0] for animal in listaAnimais)

# print(dicEspecies)
# # Counter({'leao': 3, 'javali': 1, 'hiena': 1})



# from collections import Counter

# numeros = dict()
# listNumeros =list()
# soma = 0

# while True:

#     numeros.clear()
#     numEntrada = int(input("Digite um número:"))

#     if numEntrada <= 0:
#         break
#     else:
#         numeros[numEntrada] = 1
#         listNumeros(numeros.copy())

# print(listNumeros)


# # dicEspecies = Counter(animal[0] for animal in listNumeros)

# # print(dicEspecies)




# for x in range(0, 3):
#         n = int(input("Digite o {}° valor: ".format(x+1)))
#         # y = list(dicionario["Campo2"])
#         # y.append(n)
#         # dicionario["Campo2"] = tuple(y)

#         y = list(dicionario["Campo2"])
#         y[x] = n
#         dicionario["Campo2"] = tuple(y)