import os # importa o módulo os
import random # importa o módulo random

class No: # Classe que representa um nó da lista
    def __init__(self, valor): # Construtor da classe
        self.valor = valor # Atributo que guarda o valor do nó
        self.proximo = None # Atributo que guarda o próximo nó

    def mostrar_no(self): # Método que mostra o valor do nó
        print(self.valor) # Mostra o valor do nó
        
class ListaEncadeada: # Classe Lista Encadeada

    def __init__(self): # Construtor da classe
        self.primeiro = None # Atributo que guarda o primeiro nó da lista


    def inserir_inicio(self, valor): # insere um valor no inicio da lista
        novo = No(valor) # cria um novo nó
        novo.proximo = self.primeiro # o próximo do novo nó é o primeiro da lista
        self.primeiro = novo # o primeiro da lista é o novo nó


    def mostra_item(self, posicao): # mostra o valor da posição
        if self.primeiro == None: # se a lista estiver vazia
            print("Lista vazia")
        else: 
            no = self.primeiro # inicia o no com o primeiro da lista
            i = 0 # inicia o contador com 0
            while no != None and i < posicao: # enquanto o no não for nulo e o contador for menor que a posição
                no = no.proximo # percorre a lista
                i += 1 # incrementa o contador
            if no != None: # se o no não for nulo
                no.mostrar_no() # mostra o valor do no
            else: # se o no for nulo
                print("Posição inválida") # imprime mensagem de erro
                

    def pegar_valor(self, posicao): # retorna o valor da posição
        if self.primeiro == None: # se a lista estiver vazia
            print("Lista vazia") # imprime mensagem de erro
        else: # se a lista não estiver vazia
            no = self.primeiro # inicia o no com o primeiro da lista
            i = 0 # inicia o contador com 0
            while no != None and i < posicao: # enquanto o no não for nulo e o contador for menor que a posição
                no = no.proximo # percorre a lista
                i += 1 # incrementa o contador
            if no != None: # se o no não for nulo
                return no.valor # retorna o valor do no
            else: # se o no for nulo
                print("Posição inválida") # imprime mensagem de erro
                
            

frasesDoGame = ListaEncadeada() # Lista de frases do jogo
frasesDaMain = ListaEncadeada() # Lista de frases do jogo
listaSorteio = ListaEncadeada() # Lista de numeros sortiados

frasesDoGame.inserir_inicio("Sem comentários...") 
frasesDoGame.inserir_inicio("Pelo amor de Deus...")
frasesDoGame.inserir_inicio("Você é a vergonha da profissão")
frasesDoGame.inserir_inicio("Sortudo")
frasesDoGame.inserir_inicio("Cagão")

frasesDaMain.inserir_inicio("\nValor muito alto. Tente novamente")
frasesDaMain.inserir_inicio("\nValor muito baixo. Tente novamente")
frasesDaMain.inserir_inicio("\nQue resposta sem noção em meu amigo!")


def entradaDeDados(text): # Função que recebe entrada de dados
  e = int(input(text))
  return e 

def statusGame(tentativas): # Função que verifica o status do jogo
    if(tentativas == 1 or tentativas == 0):
        resp = frasesDoGame.pegar_valor(0)
    elif(tentativas > 1 and tentativas <= 3):
        resp = frasesDoGame.pegar_valor(1)
    elif(tentativas > 3 and tentativas <= 5):
        resp = frasesDoGame.pegar_valor(2)
    elif(tentativas > 5 and tentativas <= 7):
        resp = frasesDoGame.pegar_valor(3)
    elif(tentativas > 7):
        resp = frasesDoGame.pegar_valor(4)
    return print(f'\nSTATUS DA PARTIDA: {resp}')


def main(): # Função principal

    print(f'\n{26 * "=="}\n\nBem vindo ao jogo de adivinhação!\n\n{26 * "=="}\n') # Mensagem de boas vindas

    cont = 0 #contador de tentativas

    inicio = entradaDeDados("Informe um valor de inicio: ") # Valor inicial
    fim = entradaDeDados("Informe um valor de fim: ") # Valor final

    if (inicio > fim): # Verifica se o valor inicial é maior que o valor final
        os.system('cls') or None
        print(f'\n{26 * "=="}\n')
        print("O valor de fim deve ser maior que o valor de inicio")
        main() # chama a função main() novamente

    listaSorteio.inserir_inicio(random.randint(inicio, fim)) # insere um valor aleatório na lista

    while True: # loop infinito

      resposta = entradaDeDados(f'\n{cont + 1}º tentativa: ') # entrada de dados

      if(resposta > fim): # Verifica se o valor é maior que o valor final
          frasesDaMain.mostra_item(0)
          cont = cont + 1
      elif(resposta < inicio): # Verifica se o valor é menor que o valor inicial
          frasesDaMain.mostra_item(0)
          cont = cont + 1
      elif(resposta < inicio): # Verifica se o valor é menor que o valor inicial
          frasesDaMain.mostra_item(1)
          cont = cont + 1
      elif(resposta<listaSorteio.pegar_valor(0)): # Verifica se o valor é menor que o valor sorteado
        frasesDaMain.mostra_item(1)
        cont = cont + 1
      elif(resposta>listaSorteio.pegar_valor(0)): # Verifica se o valor é maior que o valor sorteado
        frasesDaMain.mostra_item(2)
        cont = cont + 1
      elif(resposta==listaSorteio.pegar_valor(0)): # Verifica se o valor é igual ao valor sorteado
        cont = cont + 1

        print(f'\n{23 * "=="}\nVocê acertou!\n\n{cont} tentativas\n\nPontuação: {1000 - cont * 50}')
        statusGame(cont)
        print(f'{23 * "=="}\n')
        break
    

main() # chama a função main()