# Criado por: profa. Divani Barbosa Gavinier
# Curriculo Lattes: http://lattes.cnpq.br/8503400830635447
# divanibarbosa@gmail.com

class HashLinearColisao:

     def __init__(self,tam):
          self.tab = {} # cria um dicionario vazio
          self.tam_max = tam # tamanho da tabela hash

     def funcaohash(self, chave):
          v = int(chave) # converte para inteiro
          return (v%int(self.tam_max)) # retorna o resto da divisao do valor por o tamanho da tabela

     def cheia(self):
          return len(self.tab) == self.tam_max # se o tamanho da tabela for igual ao tamanho maximo

     def imprime(self):
          for i in self.tab: # percorre toda a tabela
               print("Hash[%d] = " %i, end="") # imprime a posição
               print (self.tab[i]) # imprime o item

     def busca_hash(self, chave):
          pos = self.funcaohash(chave) # pega a posicao
          if self.tab.get(pos) == None: # se esta posição não existe
               return -1 #saida imediata
          if self.tab[pos] == chave: # se o item esta na posição indicada pela função hash
               return pos # retorna a posição
          else:
               for i in self.tab: # busca do item em toda hash (pois ele pode ter sido inserido apos colisão)
                    if self.tab[i]==chave: # se o item esta na hash
                         return i # retorna a posição
          return -1

     def busca_binaria(self, chave):
          inicio = 0
          fim = len(self.tab) - 1
          while inicio <= fim:
               meio = (inicio + fim) // 2
               if self.tab[meio] == chave:
                    return meio
               if self.tab[meio] < chave:
                    inicio = meio + 1
               else:
                    fim = meio - 1
          return -1

     def busca_sequencial(self, chave):
          for i in self.tab:
               if self.tab[i] == chave:
                    return i
          return -1

     def insere(self, item):
          if self.cheia():
               print("-> ATENÇÃO Tabela Hash CHEIA")
               return
          pos = self.funcaohash(item)
          if self.tab.get(pos) == None: # se posicao vazia
               self.tab[pos] = item
               # print("-> Inserido HASH[%d]" %pos)
          else: # se posicao ocupada
               print("-> Ocorreu uma colisao na posicao %d" %pos)
               while True:
                    if self.tab[pos] == item: # se o item ja foi cadastrado
                         print("-> ATENCAO Esse item ja foi cadastrado")
                         return
                    if pos == (self.tam_max - 1):
                         pos = -1
                    pos = pos + 1 # incrementa mais uma posição
                    if self.tab.get(pos) == None:
                         self.tab[pos] = item
                         print("-> Inserido apos colisao HASH[%d]" %pos)
                         break              
# fim Classe HashLinearColisao

tamanhoHash = 100
tab = HashLinearColisao(tamanhoHash)

for i in range (100):
     tab.insere(i+5)

print(tab.busca_hash(80))

print(tab.busca_sequencial(80))