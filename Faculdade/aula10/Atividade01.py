import random 
import time 
import numpy as np

class VetorNaoOrdenado:
  def __init__(self, capacidade):                        # Método construtor, sendo o único parâmetro capacidade para determinar vetor de tamanho fixo.
    self.capacidade = capacidade                         # Atributo para a classe, recebe parâmetro capacidade.
    self.ultimaPosicao = -1                              # Armazena onde está o último elemento do vetor.
    self.valores = np.empty(self.capacidade, dtype=int)  # Dados do vetor, cria vetor vazio com a capacidade e tipo de dado definido.

  # Mostrar todos os valores da lista.
  # O(n)
  def imprimir(self):  # Não recebe parâmetro.
    if self.ultimaPosicao == -1:
      print('O vetor está vazio')
    else:
      for i in range(self.ultimaPosicao + 1):
        print(i, ' - ', self.valores[i])

  # Inserir um novo elementos ao final da lista (ultimaPosicao).
  # O(1) - O(2)
  def inserir(self, valor):
    if self.ultimaPosicao == self.capacidade - 1:
      print('Capacidade máxima atingida')
    else:
      self.ultimaPosicao += 1
      self.valores[self.ultimaPosicao] = valor

  # Busca um valor na lista e indicar sua posição.
  # O(n)
  def pesquisar(self, valor):
    for i in range(self.ultimaPosicao + 1):
      if valor == self.valores[i]:
        return i
    return -1  # Caso o valor não seja encontrado.  

  #Exclui um valor da lista, reorganiza valores posteriores.
  # O(n)
  def excluir(self, valor):
    posicao = self.pesquisar(valor)
    if posicao == -1:
      return -1  # Caso o valor não seja encontrado.
    else:
      for i in range(posicao, self.ultimaPosicao):
        self.valores[i] = self.valores[i + 1]  # Realiza o deslocamento dos elementos posteriores uma posição à frente.
      self.ultimaPosicao -= 1  # Indica que a lista diminuiu em um item.


  # <----- NOVAS FUNCIONALIDADES ----->

  # Gera valores aleatórios entre 0 e 999 para o vetor/lista.
  def gera_dados(self, limite):
    for i in range(limite-1):
      # Insere valores aleatórios. 
      self.inserir(random.randrange(0, 999))  # Gera um número randômico em uma faixa, entre 0 e 555. 
    self.inserir(999)  # Último valor inserido, para controle.
    self.ordena_bolha()  # Ordena valores por ordem crescente.
    self.imprimir()
  
   # Buscar binária por um valor.
  def busca_binaria(self, valor):
    inicio = 0
    fim = self.ultimaPosicao
    while inicio <= fim:
      meio = int((fim + inicio) / 2)  # Encontra a posição do meio.
      if self.valores[meio] == valor:  # Caso valor já esxista na lista, informa.
        return meio
      elif valor < self.valores[meio]:  # Se valor menor do que o valor que está no meio, reposiciona o marcador do fim. Caso contrário, reposiciona o marcador do início.
        fim = meio - 1
      else:
        inicio = meio + 1 
    return -1

  
  # Ordena o vetor pelo método Bubble Sort.
  # O princípio do Bubble Sort é a troca entre posições consecutivas, fazendo com que valores mais altos (ou mais baixos) "borbulhem" para o final do vetor.
  def ordena_bolha(self): 
    troca = True
    while troca:  # Enquanto houver ao menos uma troca, continua o processo.
      troca = False
      for i in range(self.ultimaPosicao):
        if self.valores[i] > self.valores[i + 1]:  # Se o valor da esquerda é maior, então troca.
          aux = self.valores[i]
          self.valores[i] = self.valores[i + 1]
          self.valores[i + 1] = aux
          troca = True

  # Informa tempo de execução para encontrar um valor no vetor.  
  def tempo_execucao(self, valor):  
    antes = time.time()  # Timestamp de antes de chamar a busca, em segundos.
    pos = self.pesquisar(valor)
    segundos = time.time() - antes
    print('Levou {} segundos'.format(segundos))

    if pos >= 0:
      print('Valor encontrado na posição {}'.format(pos))
    else:
      print('Valor não encontrado')  