#============================================= REFERÊNCIAS =================================================#

# -> Utilizamos os conceitos teóricos do vídeo.

# https://www.youtube.com/watch?v=wBReEzdR7So&ab_channel=Programa%C3%A7%C3%A3oDescomplicadaLinguagemC

#=========================================================================================================#

#========================================= INTEGRANTES DO GRUPO ==========================================#

# -> Kaio Vinicius de Paiva Rodrigues 
# -> João Vitor Tremea Laufer
# -> Gabriel da Silva Santos
# -> Lázaro machado de Souz
# -> Pedro Henrique Leitão
# -> Tiago da Rosa Gularte
# -> Juliana Machado

#=========================================================================================================#



import os

def limpa_tela():
     os.system('cls' if os.name == 'nt' else 'clear')


#=========================================================================================================#



class tabela:

    #==================================================================================================================================================#
     def __init__(self,tam):                                                    # construtor
          self.tab = {}                                                         # cria um dicionario
          self.tam_max = tam                                                    # define o tamanho da tabela para minimizar as colisões 
    #==================================================================================================================================================#



    #==================================================================================================================================================#
     def funcaohash(self, chave):                                               # função hash para a tabela hash (Método da Divisão / método da congruência linear)
          v = int(chave)                                                        # Essa função hasd produz um espalhamento uniforme das posições 
          return (v%int(self.tam_max))                                          # retorna o resto da divisão da chave por tamanho da tabela
    #==================================================================================================================================================#



    #==================================================================================================================================================#
     def cheia(self):                                                           # verifica se a tabela esta cheia
          return len(self.tab) == self.tam_max                                  # retorna True se o tamanho da tabela for igual ao tamanho maximo
    #==================================================================================================================================================#



    #==================================================================================================================================================#
     def vazia(self):                                                           # verifica se a tabela esta vazia
          return len(self.tab) == 0
    #==================================================================================================================================================#



    #==================================================================================================================================================#
     def imprime(self):                                                         # imprime a tabela hash
          for i in self.tab:                                                    # percorre toda a tabela
               print("[%d] = " %i, end="")                                      # imprime a posição
               print (self.tab[i])                                              # imprime o item
    #==================================================================================================================================================#



    #==================================================================================================================================================#
    # A busca é realizada dentro da própria tabela, o que permite uma recuperação mais rápida
    # Ao invés de acessamos ponteiros, calculamos a sequência de posições a serem armazenadas  

     def busca_hash(self, chave):                                               
          pos = self.funcaohash(chave)                                          # calcula a posição
          if self.tab.get(pos) == None:                                         # se esta posição não existe
               return -1                                                        #saida imediata
          if self.tab[pos] == chave:                                            # se o item esta na posição indicada pela função hash
               return pos                                                       # retorna a posição 
          else:
               for i in self.tab:                                               # busca do item em toda hash (pois ele pode ter sido inserido apos colisão)
                    if self.tab[i]==chave:                                      # se o item esta na tabela
                         return i                                               # retorna a posição
          return -1

     def busca_binaria(self, chave):                                            # busca binaria
          inicio = 0                                                            # posicao inicial
          fim = len(self.tab) - 1                                               # posicao final
          while inicio <= fim:                                                  # enquanto a posicao inicial for menor ou igual a posicao final
               meio = (inicio + fim) // 2                                       # calcula a posicao do meio
               if self.tab[meio] == chave:                                      # se o item esta no meio
                    return meio                                                 # retorna a posicao
               elif chave < self.tab[meio] :                                    # se a chave for menor que o item do meio
                    fim = meio - 1                                              # posicao final recebe a posicao do meio - 1
               else:                                                            # se a chave for maior que o item do meio
                    inicio = meio + 1                                           # posicao inicial recebe a posicao do meio + 1
          return -1
      
    #==================================================================================================================================================#
     def busca_sequencial(self, chave):                                         # busca sequencial
          for i in self.tab:                                                    # percorre toda a tabela
               if self.tab[i] == chave:                                         # se o item esta na tabela
                    return i                                                    # retorna a posição
          return -1                                                             # se nao encontrou o item
    #==================================================================================================================================================#



    #==================================================================================================================================================#
    # Nessa função que fizemos o tratamento das possíveis colisões usando a técnica de
    # endereçamento aberto, essa técnica evita o uso de listas encadeadas
    # usamos essa técnica pelo fato de ser uma das que mais diminuir o número de colisões

     def insere(self, item):                                                    
          if self.cheia():                                                      # se a tabela esta cheia
               print("-> [ATENÇÃO] Tabela Hash CHEIA")                          # avisa que a tabela esta cheia
               return False                                                     # retorna falso
          pos = self.funcaohash(item)                                           # calcula a posição
          if self.tab.get(pos) == None:                                         # se posicao vazia
               self.tab[pos] = item                                             # insere o item na posicao
               #print("-> Inserido HASH[%d]" %pos)
          else:                                                                 # se posicao ocupada
               print("->[ATENÇÃO] Ocorreu uma colisao na posicao %d" %pos)      # avisa que ocorreu uma colisao
               while True:                                                      # enquanto o item nao for inserido
                    if self.tab[pos] == item:                                    # se o item ja foi cadastrado
                         print("-> ATENCAO Esse item ja foi cadastrado")        # avisa que o item ja foi cadastrado
                         return False                                           # retorna falso
                    if pos == (self.tam_max - 1):                               # se a posicao for igual ao tamanho maximo
                         pos = -1                                               # posicao recebe -1
                    pos = pos + 1                                               # incrementa mais uma posição
                    if self.tab.get(pos) == None:                               # se a posicao esta vazia 
                         self.tab[pos] = item                                   # insere o item na posicao
                         print("-> Inserido apos colisao HASH[%d]" %pos)        # avisa que o item foi inserido
                         break # sai do laço
  #==================================================================================================================================================#


def main():
  
    #==================================================================================================================================================#
     limpa_tela()
     print(f'{50*"="}\n{12* " "}A BUSCA PELA EFICIENCIA\n{50*"="}\n')
     tamanho = int(input("-> Porfavor informe o tamanho da tabela: "))
     limpa_tela()
     tab = tabela(tamanho)
     #==================================================================================================================================================#



     #==================================================================================================================================================#
     while True:
          print(f'{50*"="}\n{23* " "}MENU\n{50*"="}\n')
          op = int(input(f'1 - Inserir\n2 - Buscar\n3 - Imprimir\n0 - Sair\n\nDigite a opção desejada: '))

          if op == 1:
               limpa_tela()
               entrada = int(input("-> Informe a quantidade de valores que deseja inserir: "))
               limpa_tela()
               if entrada > tamanho:
                    limpa_tela()
                    print("-> [ATENÇÃO] Quantidade de valores maior que o tamanho da tabela")
                    continue
               else:
                    for i in range(entrada):
                         tab.insere(i)
                 
          elif op == 2:
               if tab.vazia():
                    limpa_tela()
                    print("-> [ATENÇÂO] Tabela vazia")
               else:
                    limpa_tela()
                    entrada2 = int(input("-> Informe o número a ser buscado nas 3 formas de busca: "))
                    limpa_tela()
                    if entrada2 > tamanho:
                         limpa_tela()
                         print("-> [ATENÇÂO] Número maior que o tamanho da tabela")
                         continue
                    else:
                         print("\n\n\n")
                         print(f'{20 * "="}BUSCA SEQUENCIAL{20 * "="}\n')
                         tab.busca_sequencial(entrada2)
                         print("\n")
                         print(f'{20 * "="}BUSCA BINARIA{20 * "="}\n')
                         tab.busca_binaria(entrada2)
                         print("\n")
                         print(f'{20 * "="}BUSCA HASH{20 * "="}\n')
                         tab.busca_hash(entrada2)
                         print("\n\n\n")
          elif op == 3:
               if tab.vazia():
                    limpa_tela()
                    print("-> [ATENÇÂO] Tabela vazia")
               else:
                    tab.imprime()

          elif op == 0:
               break
    #==================================================================================================================================================#