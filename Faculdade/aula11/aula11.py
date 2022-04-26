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

ordenacao_bolha(numeros)
ordenacao_insert(numeros)
ordenacao_selecao_direta(numeros)