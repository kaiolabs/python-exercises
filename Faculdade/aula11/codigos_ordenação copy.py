import numpy as np
import random as rd

# Metodo de ordenação 1

def ordenacao_insert(lista): # def que vai ordenar a lista com o algoritmo de inserção que funciona em por meio de um loop for e um if para verificar se o valor de i é menor que o valor de i+1 e se for ele troca os valores de i e i+1 entre si 
    if len(lista) <= 1:# se a lista for menor ou igual a 1 ele retorna a lista
        return lista
    else:
        for i in range(1, len(lista)): # loop de ordenação de 1 até n-1
            j = i # j recebe o valor de i
            while j > 0 and lista[j] < lista[j - 1]: # loop de busca do menor valor para troca de valores de i e i-1 
                lista[j], lista[j - 1] = lista[j - 1], lista[j] # troca os valores de i e i-1 entre si atraves do valor de j usando o valor de j-1 
                j -= 1 # j recebe o valor de j-1
        return lista



# Metodo de ordenação 2

def ordenacao_bolha(lista): 
    if len(lista) <= 1:# se a lista for menor ou igual a 1 ele retorna a lista
        return lista
    else:
        for i in range(len(lista) - 1, 0, -1): # loop de ordenação de n-1 até 1 e decrementa 1 em cada loop 
            for j in range(i): # loop de busca do menor valor que fara o troca de valores de i e j 
                if lista[j] > lista[j + 1]: # se o valor de j for maior que o valor de j+1 ele fara o troca deles
                    lista[j], lista[j + 1] = lista[j + 1], lista[j] # troca os valores de j e j+1 entre si para fazer a ordenação 
        return lista



# Metodo de ordenação 3

def ordenacao_selecao_direta(lista):
    if len(lista) <= 1:# se a lista for menor ou igual a 1 ele retorna a lista
        return lista
    else:
        for i in range(len(lista) - 1): # loop de ordenação de 1 até n-1
            menor = i # menor recebe o valor de i
            for j in range(i + 1, len(lista)): # loop de busca do menor valor
                if lista[j] < lista[menor]: # se o valor de j for menor que o valor de menor ele fara o troca deles
                    menor = j # menor recebe o valor de j
            lista[i], lista[menor] = lista[menor], lista[i] # troca os valores de i e menor entre si 
        return lista





# Metodo de ordenação 4

def quick_sort(lista):
    if len(lista) <= 1: # se o tamanho da lista for menor ou igual a 1 ele retorna a lista 
        return lista
    else:
        pivo = lista.pop() # pivo recebe o ultimo valor da lista
        menor = [] # menor recebe uma lista vazia
        maior = [] # maior recebe uma lista vazia
        for i in lista: # loop de busca do menor valor
            if i <= pivo: # se o valor de i for menor ou igual ao pivo ele fara o append na lista menor
                menor.append(i)
            else: # se não ele fara o append na lista maior
                maior.append(i)
        return quick_sort(menor) + [pivo] + quick_sort(maior) # retorna a lista ordenada com o pivo e as listas de menor e maior







# Metodo de ordenação 5

def countingSort(arr, exp1):

	n = len(arr)
	output = [0] * (n)
	count = [0] * (10)
	
	for i in range(0, n):
		index = (arr[i]/exp1)
		count[int((index)%10)] += 1

	for i in range(1,10):
		count[i] += count[i-1]

	i = n-1# Build the output array
	while i>=0:
		index = (arr[i]/exp1)
		output[ count[ int((index)%10) ] - 1] = arr[i]
		count[int((index)%10)] -= 1
		i -= 1
	
	i = 0
	for i in range(0,len(arr)):
		arr[i] = output[i]


def radixSort(arr):
    if len(arr) <= 1: # se o tamanho da lista for menor ou igual a 1 ele retorna a lista
        return arr
    else:
        max1 = max(arr)
        exp = 1
        while max1/exp > 0:
            countingSort(arr,exp)
            exp *= 10





# Metodo de ordenação 6

def shell_sort(lista):
    if len(lista) <= 1: # se o tamanho da lista for menor ou igual a 1 ele retorna a lista
        return lista
    else:
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




tamanho_pequeno = 1000
tamanho_medio = 10000
tamanho_grande = 50000
tamanho_supergrande = 100000


# Grupo 1 de listas

# números aleatórios
caso_de_teste1_numeros_aleatorios = np.array(np.random.randint(0, 1000, 10))

# números crecentes
caso_de_teste2_numeros_crecentes = np.array(range(1, 10 + 1))

# números decrescentes
caso_de_teste3_numeros_decrescentes = np.array(range(10, 0, -1))

# números repetidos
caso_de_teste4_numeros_repetidos = np.array(np.random.randint(1, 3, 10))

# lista vazia
caso_de_teste5_lista_vazia = np.array([])

# lista com um elemento
caso_de_teste6_lista_um_elemento = np.array([1])

# muitos números repetidos
caso_de_teste7_muitos_numeros_repetidos = np.array(np.random.randint(1, 10, 100))

# lista longa
caso_de_teste8_lista_longa = np.array(np.random.randint(0, 10000, 1000))


# # lista com números flooat
# caso_de_teste9_lista_com_numeros_float = np.array(np.random.random(0, 1000, 10))

copy = np.copy(caso_de_teste1_numeros_aleatorios)




# Grupo 2 de listas



def Testes_altomatizados():

    # números aleatórios
    caso_de_teste1_numeros_aleatorios = np.array(np.random.randint(0, 1000, 10))

    # números crecentes
    caso_de_teste2_numeros_crecentes = np.array(range(1, 10 + 1))

    # números decrescentes
    caso_de_teste3_numeros_decrescentes = np.array(range(10, 0, -1))

    # números repetidos
    caso_de_teste4_numeros_repetidos = np.array(np.random.randint(1, 3, 10))

    # lista vazia
    caso_de_teste5_lista_vazia = np.array([])

    # lista com um elemento
    caso_de_teste6_lista_um_elemento = np.array([1])

    # muitos números repetidos
    caso_de_teste7_muitos_numeros_repetidos = np.array(np.random.randint(1, 10, 100))

    # lista longa
    caso_de_teste8_lista_longa = np.array(np.random.randint(0, 10000, 1000))


    op = input(int(f'Qual metodo de ordenação deseja testar?\n1 - Bubble Sort\n2 - Selection Sort\n3 - Insertion Sort\n4 - Quick Sort\n5 - Counting Sort\n6 - Radix Sort\n7 - Shell Sort\n'))

    # Metodo de ordenação 1
    if op == 1:
        print(f'=============== TESTE números aleatórios ===============')
        ordenacao_insert(np.copy(caso_de_teste1_numeros_aleatorios))
        print(f'=============== TESTE números crecentes ===============')
        ordenacao_insert(np.copy(caso_de_teste2_numeros_crecentes))
        print(f'=============== TESTE números decrescentes ===============')
        ordenacao_insert(np.copy(caso_de_teste3_numeros_decrescentes))
        print(f'=============== TESTE números repetidos ===============')
        ordenacao_insert(np.copy(caso_de_teste4_numeros_repetidos))
        print(f'=============== TESTE lista vazia ===============')
        ordenacao_insert(np.copy(caso_de_teste5_lista_vazia))
        print(f'=============== TESTE lista com um elemento ===============')
        ordenacao_insert(np.copy(caso_de_teste6_lista_um_elemento))
        print(f'=============== TESTE muitos números repetidos ===============')
        ordenacao_insert(np.copy(caso_de_teste7_muitos_numeros_repetidos))
        print(f'=============== TESTE lista longa ===============')
        ordenacao_insert(np.copy(caso_de_teste8_lista_longa))

    # Metodo de ordenação 2
    elif metodo == 'ordenacao_bolha':
    # Metodo de ordenação 3
        ordenacao_bolha(lista)
    elif metodo == 'ordenacao_selecao_direta':
    # Metodo de ordenação 4
        ordenacao_selecao_direta(lista)
    elif metodo == 'quick_sort':
    # Metodo de ordenação 5
        quick_sort(lista)
    elif metodo == 'radixSort':
    # Metodo de ordenação 6
        radixSort(lista)
    elif metodo == 'shell_sort':
    # Metodo de ordenação 7
        shell_sort(lista)


Testes_altomatizados()