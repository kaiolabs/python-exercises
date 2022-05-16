import numpy as np
import random as rd

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


# números aleatórios
caso_de_teste1_numeros_aleatorios = np.array(np.random.randint(0, 1000, 10))



def teste(ndefinicao):
    
  print(f'\n================= TESTE ordenação insert =====================\n')

  print(f'\n=============== TESTE números aleatórios =====================')
  
  definicao(np.copy(caso_de_teste1_numeros_aleatorios))

  print(f'\nANTES DE ORDENAR {np.copy(caso_de_teste1_numeros_aleatorios)}\n')
  print(f'\nDEPOIS DE ORDENAR{definicao(np.copy(caso_de_teste1_numeros_aleatorios))}\n')



teste(ordenacao_bolha)