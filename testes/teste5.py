# f = open('dados.txt', 'r+')
f = open("dados.txt", "r")
# for line in f:


# def busca_sequencial(chave): # busca sequencial
#     for line in f: # percorre toda a tabela
#         print(line)
#         if line == chave: # se o item esta na tabela
#             return line # retorna a posição
#         else:
#             return -1 # se nao encontrou o item

# print(busca_sequencial('3033'))

# with open("arquivo.txt","r+") as arquivo:

#     arquivo.write("Estou escrevendo")

#     arquivo.readline()

arq = open("dados.txt", "r")
linhas = arq.readlines()
teste = '5170'
for linha in linhas:
    if teste in linha:
        print(linha)
        break