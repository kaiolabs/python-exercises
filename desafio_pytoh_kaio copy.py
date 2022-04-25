import random
import os

file = open("dados.txt","r") 

def tamanhoMax():
     Counter = 0
     Content = file.read() 
     CoList = Content.split("\n") 
          
     for i in CoList: 
          if i: 
               Counter += 1
                         
     return Counter

class tablinear:

     def __init__(self): # construtor
          self.tab = open("dados.txt","r") 
          self.tam_max = tamanhoMax() # define o tamanho da tabela

     def funcaohash(self, chave): # função hash para a tabela hash
          v = int(chave) 
          return (v%int(self.tam_max)) # retorna o resto da divisão da chave por tamanho da tabela

     def imprime(self): # imprime a tabela hash
          for i in self.tab: # percorre toda a tabela
               print("Hash[%d] = " %i, end="") # imprime a posição
               print (self.tab[i]) # imprime o item

     def busca_hash(self, chave): # busca na tabela hash
          pos = self.funcaohash(chave) # calcula a posição
          if self.tab.get(pos) == None: # se esta posição não existe
               return -1 #saida imediata
          if self.tab[pos] == chave: # se o item esta na posição indicada pela função hash
               return pos # retorna a posição 
          else:
               for i in self.tab: # busca do item em toda hash (pois ele pode ter sido inserido apos colisão)
                    if self.tab[i]==chave: # se o item esta na tabela
                         return i # retorna a posição
          return -1

     def busca_binaria(self, chave): # busca binaria
          inicio = 0 # posicao inicial
          fim = tamanhoMax() - 1 # posicao final
          while inicio <= fim: # enquanto a posicao inicial for menor ou igual a posicao final
               meio = (inicio + fim) // 2 # calcula a posicao do meio
               if self.tab[meio] == chave: # se o item esta no meio
                    return meio # retorna a posicao
               elif chave < self.tab[meio] : # se a chave for menor que o item do meio
                    fim = meio - 1 # posicao final recebe a posicao do meio - 1
               else: # se a chave for maior que o item do meio
                    inicio = meio + 1 # posicao inicial recebe a posicao do meio + 1
          return -1

     def busca_sequencial(self, chave):
          linhas = file.readlines()
          for linha in linhas:
               if str(chave) in linha:
                    return linha
               else:
                    return -1


     def geraValores(self, tamanhoDaLista): # insere na tabela hash
          lista = []
          for i in range(tamanhoDaLista+1):
               lista.append(random.randrange(3000, (tamanhoDaLista*1000))) 

          def remove_repetidos(lista):
               l = []
               for i in lista:
                    if i not in l:
                         l.append(i)
               l.sort()
               return l

          lista = remove_repetidos(lista)

          with open("dados.txt", "w") as dados:
               for i in range(len(lista)):
                    dados.write(str(lista[i]) + "\n")


