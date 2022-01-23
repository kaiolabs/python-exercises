# i=[[33,59],[34,60],[35,61],[36,62],[37,63],[38,64],[39,65],[40,66],[41,67],[42,68],[43,69],[44,70],[45,71],[46,72],[47,73],[48,74],[49,75],[50,76],[51,77],[52,78],[53,79],[54,80],[55,81],[56,82],[57,83],[58,84]]
# senha="senhasenha"
# x=""
# k=""
# y=0
# for a in senha:
#     j=(ord(a)-97)
#     x+=(chr(i[j][y]))
#     y+=1
#     if(y>1):
#         y=0
# print (x)

# for w in x:
#     k = ord(w)
#     for lista in i:
#         if k in lista:
#             print("j =",i.index(lista),"y =",lista.index(k),"letra =",chr(i.index(lista)+97))




# Reservas[9][7] = 80
# cont = 0

# print('='*50)
# for l in range(0, 10):
#     for c in range(0, 8):
#         print(f'[{Reservas[l][c]}]', end='')
#         cont + 1
#     print()








# matriz = [[0,0,0],[0,0,0],[0,0,0]]

# for i in range(len(matriz)):
#    for j in range(len(matriz[i])):
#       matriz[i][j] = int(input("informe o numero: "))

# print("matriz informada:")

# for i in range(len(matriz)):
#    for j in range(len(matriz[i])):
#       print(matriz[i][j],end=" ")
#    print()

# #encontrar o menor elemento
# linha = 0;
# col = 0;
# for i in range(len(matriz)):
#    for j in range(len(matriz[i])):
#       if(matriz[i][j]<matriz[linha][col]):
#          linha = i
#          col = j

# print(f"Menor elemento: {matriz[linha][col]}")
# print(f"Linha: {linha+1}")
# print(f"coluna: {col+1}")



















# inventario = {'banana': 50, 'laranja': 12, 'melancia': 7, 'kiwi': 23}

# total = 0
# for valor in inventario.values():
#     total += valor

# print("Temos %d frutas no inventario."%(total))











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