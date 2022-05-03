numeros = [ 76,  83,  2,  12,  45,  9,  74,  3,  40,  5,  
            47,  81,  6,  53,  68,  7,  14,  10,  11,  13,  
            15,  16,  17,  18,  19,  20,  21,  22,  23,  24,  
            25,  26,  27,  28,  29,  30,  31,  32,  33,  34,  
            35,  36,  37,  38,  39,  41,  42,  43,  44,  46,  
            48,  49,  50,  51,  52,  54,  55,  56,  57,  58,  
            59,  60,  61,  62,  63,  64,  65,  66,  67,  69,  
            70,  71,  72,  73,  75,  77,  78,  79,  80,  82,  
            84,  85,  86,  87,  88,  89,  90,  91,  92,  93,  
            94,  95,  96,  97,  98,  99,  100, 101, 102, 103, 
            104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 
            114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 
            124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 
            134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 
            144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 
            154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 
            164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 
            174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 
            184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 
            194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 
            204, 205, 206,]


import random
import numpy as np

def ordenacao_insert(lista): # def que vai ordenar a lista com o algoritmo de inserção que funciona em por meio de um loop for e um if para verificar se o valor de i é menor que o valor de i+1 e se for ele troca os valores de i e i+1 entre si 
    for i in range(1, len(lista)): # loop de ordenação de 1 até n-1
        j = i # j recebe o valor de i
        while j > 0 and lista[j] < lista[j - 1]: # loop de busca do menor valor para troca de valores de i e i-1 
            lista[j], lista[j - 1] = lista[j - 1], lista[j] # troca os valores de i e i-1 entre si atraves do valor de j usando o valor de j-1 
            j -= 1 # j recebe o valor de j-1
    return lista


def ordenacao_bolha(lista): 
    for i in range(len(lista) - 1, 0, -1): # loop de ordenação de n-1 até 1 e decrementa 1 em cada loop 
        for j in range(i): # loop de busca do menor valor que fara o troca de valores de i e j 
            if lista[j] > lista[j + 1]: # se o valor de j for maior que o valor de j+1 ele fara o troca deles
                lista[j], lista[j + 1] = lista[j + 1], lista[j] # troca os valores de j e j+1 entre si para fazer a ordenação 
    return lista

def ordenacao_selecao_direta(lista):
    for i in range(len(lista) - 1): # loop de ordenação de 1 até n-1
        menor = i # menor recebe o valor de i
        for j in range(i + 1, len(lista)): # loop de busca do menor valor
            if lista[j] < lista[menor]: # se o valor de j for menor que o valor de menor ele fara o troca deles
                menor = j # menor recebe o valor de j
        lista[i], lista[menor] = lista[menor], lista[i] # troca os valores de i e menor entre si 
    return lista


# Quick Sort


def quick_sort(lista):
    if len(lista) <= 1: # se o tamanho da lista for menor ou igual a 1 ele retorna a lista 
        return lista
    pivo = lista.pop() # pivo recebe o ultimo valor da lista
    menor = [] # menor recebe uma lista vazia
    maior = [] # maior recebe uma lista vazia
    for i in lista: # loop de busca do menor valor
        if i <= pivo: # se o valor de i for menor ou igual ao pivo ele fara o append na lista menor
            menor.append(i)
        else: # se não ele fara o append na lista maior
            maior.append(i)
    return quick_sort(menor) + [pivo] + quick_sort(maior) # retorna a lista ordenada com o pivo e as listas de menor e maior

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivo = lista[0]
    menores = [x for x in lista if x < pivo]
    maiores = [x for x in lista if x > pivo]
    return quick_sort(menores) + [pivo] + quick_sort(maiores)

# marge sort

def marge_sort(lista):
    if len(lista) <= 1:
        return lista
    meio = len(lista) // 2
    esquerda = marge_sort(lista[:meio])
    direita = marge_sort(lista[meio:])
    return merge(esquerda, direita)

def merge_sort(lista):
    if len(lista) <= 1: # se o tamanho da lista for menor ou igual a 1 ele retorna a lista 
        return lista
    meio = len(lista) // 2 # meio recebe o tamanho da lista dividido por 2
    return merge(merge_sort(lista[:meio]), merge_sort(lista[meio:])) # retorna a lista ordenada com o merge de duas listas


# radix sort

def radix_sort(lista):
    maximo = max(lista) # maximo recebe o maior valor da lista
    expoente = 1
    while True:
        buckets = [[] for _ in range(10)] # buckets recebe uma lista de 10 listas vazias
        for numero in lista: # loop de busca dos valores da lista
            buck_index = (numero // expoente) % 10 # buck_index recebe o valor de numero dividido por expoente e dividido por 10
            buckets[buck_index].append(numero) # buckets[buck_index] recebe o valor de numero
        if all(buckets[i] == [] for i in range(10)): # se todos os valores das listas forem vazias ele retorna a lista ordenada 
            return lista
        lista = []
        for buck in buckets: # loop de busca das listas
            lista += buck # lista recebe as listas
        expoente *= 10 # expoente recebe o expoente multiplicado por 10

def radix_sort(lista):
    maximo = max(lista) # maximo recebe o valor maximo da lista
    expoente = 1 # expoente recebe 1
    while maximo // expoente > 0: # enquanto o expoente for maior que 0 ele fara o loop 
        lista = counting_sort(lista, expoente) # lista recebe o counting_sort com o expoente
        expoente *= 10 # expoente recebe o expoente multiplicado por 10
    return lista

def radix_sort(lista):
    lista_ordenada = [] # lista_ordenada recebe uma lista vazia
    maximo = max(lista) # maximo recebe o maior valor da lista
    expoente = 1 # expoente recebe 1
    while maximo // expoente > 0: # enquanto o maximo dividido por expoente for maior que 0 ele faz o loop
        buckets = [[] for _ in range(10)] # buckets recebe uma lista de 10 listas vazias
        for i in lista: # loop de busca
            buck_index = (i // expoente) % 10 # buck_index recebe o valor do i dividido por expoente e dividido por 10 e resto da divisao
            buckets[buck_index].append(i) # buckets[buck_index] recebe a lista de i
        lista = [] # lista recebe uma lista vazia
        for buck in buckets: # loop de busca
            lista.extend(buck) # lista recebe a lista de buck
        expoente *= 10 # expoente recebe 10 vezes o valor de expoente
    return lista

def radix_sort(lista):
    maximo = max(lista) # maximo recebe o maior valor da lista
    expoente = 1 # expoente recebe 1
    while True: # loop infinito
        resultado = [] # resultado recebe uma lista vazia
        for i in range(10): # loop de busca do menor valor
            lista_filtrada = [x for x in lista if (x // expoente) % 10 == i] # lista_filtrada recebe a lista filtrada com os valores que são divisiveis por expoente 
            resultado.extend(lista_filtrada) # resultado recebe a lista filtrada
        if len(resultado) == len(lista): # se o tamanho da lista for igual ao tamanho da lista filtrada ele retorna a lista filtrada
            return resultado
        lista = resultado # lista recebe a lista filtrada
        expoente *= 10 # expoente recebe o expoente multiplicado por 10

    

def radix_sort(lista):
    maximo = max(lista) # maximo recebe o valor maximo da lista
    expoente = 1 # expoente recebe 1
    while maximo / expoente > 0: # enquanto o maximo dividido o expoente for maior que 0 ele fara o loop
        lista_ordenada = [] # lista_ordenada recebe uma lista vazia
        lista_contador = [0] * 10 # lista_contador recebe uma lista com 10 posições vazias
        for i in lista: # loop de busca do menor valor
            lista_contador[(i // expoente) % 10] += 1 # lista_contador[(i // expoente) % 10] recebe o resto da divisão de i por expoente e o modulo de 10
        for i in range(1, 10): # loop de ordenação de 1 até 9
            lista_contador[i] += lista_contador[i - 1] # lista_contador[i] recebe o valor de lista_contador[i-1] mais o valor de lista_contador[i]
        for i in range(len(lista) - 1, -1, -1): # loop de ordenação de n-1 até 1 e decrementa 1 em cada loop
            posicao = (lista[i] // expoente) % 10 # posicao recebe o resto da divisão de i por expoente e o modulo de 10
            lista_ordenada.insert(lista_contador[posicao] - 1, lista[i]) # lista_ordenada.insert(lista_contador[posicao] - 1, lista[i]) recebe o valor de lista_ordenada mais o valor de lista[i]
            lista_contador[posicao] -= 1 # lista_contador[posicao] recebe o valor de list

# shell sort

def shell_sort(lista):
    for intervalo in range(len(lista) // 2, 0, -1): # loop de busca do intervalo
        for i in range(intervalo): # loop de busca do i
            for j in range(i, len(lista), intervalo): # loop de busca do j
                if lista[j] < lista[j - intervalo]: # se o valor de j for menor que o valor de j - intervalo ele faz a troca
                    lista[j], lista[j - intervalo] = lista[j - intervalo], lista[j]

def shell_sort(lista):
    h = 1 # h recebe 1
    while h < len(lista) // 3: # enquanto h for menor que o tamanho da lista dividido por 3 ele faz o loop
        h = 3 * h + 1 # h recebe 3 vezes o valor de h mais 1
    while h >= 1: # enquanto h for maior ou igual a 1 ele faz o loop
        for i in range(h, len(lista)): # loop de busca do menor valor
            aux = lista[i] # aux recebe o valor de i
            j = i
            while j >= h and lista[j - h] > aux: # enquanto j for maior ou igual a h e lista[j-h] for maior que aux ele faz o loop
                lista[j] = lista[j - h] # lista[j] recebe lista[j-h]
                j -= h # j recebe j - h
            lista[j] = aux # lista[j] recebe o valor de aux
        h //= 3 # h recebe h dividido por 3

def shell_sort(lista):
    gap = len(lista) // 2 # gap recebe o tamanho da lista dividido por 2
    while gap > 0: # enquanto o valor de gap for maior que 0 ele faz o loop
        for i in range(gap, len(lista)): # loop de busca
            temp = lista[i] # temp recebe o valor de lista[i]
            j = i # j recebe o valor de i
            while j >= gap and lista[j - gap] > temp: # enquanto o j for maior que o gap e o valor de lista[j-gap] for maior que o valor de temp ele faz o loop
                lista[j] = lista[j - gap] # lista[j] recebe o valor de lista[j-gap]
                j -= gap # j recebe o valor de j - gap
            lista[j] = temp # lista[j] recebe o valor de temp
        gap //= 2 # gap recebe o valor de gap dividido por 2

def shell_sort(lista):
    intervalo = len(lista) // 2 # intervalo recebe o tamanho da lista dividido por 2
    while intervalo > 0: # enquanto o intervalo for maior que 0 ele fara o loop
        for i in range(intervalo, len(lista)): # loop de busca do menor valor
            temp = lista[i] # temp recebe o valor de i
            j = i
            while j >= intervalo and lista[j - intervalo] > temp: # enquanto j for maior que o intervalo e o valor de j - intervalo for maior que o valor de temp ele faz o loop
                lista[j] = lista[j - intervalo] # lista[j] recebe o valor de lista[j - intervalo]
                j -= intervalo # j recebe o valor de j - intervalo
            lista[j] = temp # lista[j] recebe o valor de temp
        intervalo //= 2 # intervalo recebe o intervalo dividido por 2



# Para testar: lista de números em ordem aleatória.
vetor1 = np.array([8, 5, 1, 7, 9, 4, 10, 3, 6, 2])

# Para testar: lista que já está ordenada.
vetor2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Para testar: uma lista em ordem decrescente.
vetor3 = np.array([10,9, 8, 7, 6, 5, 4, 3, 2, 1])

# Para testar: ...

# Para testar: uma lista longa aleatória.
vetor8 = rd.randint(0, 1000, 100)