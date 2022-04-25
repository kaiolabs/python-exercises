"""
Nomes: Cauana Dal-Berto, Eduardo Nunes, Isabelle Vargas, Guilherme Augusto
 e João Sobral.

Fábrica de Software - 2022/01
"""
#*********************************************************************************#
#*********************************************************************************#
#*********************************************************************************#

from random import randint                              #Método para gerar números aleatórios.
from numpy import empty                                 #Biblioteca para inicializar o vetor.
from os import system, name                             #Métodos para limpar a tela.
from time import process_time_ns                        #Método para comparar o tempo de busca.

#*********************************************************************************#
#*********************************************************************************#
#*********************************************************************************#

class Seq:

    def __init__(self, tam):
        self.tam = tam                                  #Define tamanho da lista.
        self.numeros = empty(self.tam, dtype=int)       #Inicializa a lista.

    def popula(self):
        for i in range(self.tam):
            n = randint(0, 10000)                        #Gera números aleatórios de 0 à 3000.
            v = self.busca(n)                           #Verifica se o valor buscado já não foi inserido.

            if v == True:                               #Se sim...
                continue
            else:                                       #Se não realiza a inserção.
                self.numeros[i] = n
             
    def mostra(self):
        for i in range(self.tam):
            if self.numeros[i] != -1:                   #Verifica se o número da posição é valido.
                print(self.numeros[i], end=" ")         #Imprime os números em linha.

            if (i % 10) == 0:                           #Quebra a linha a cada dez impressões.
                print("\n")
        
        print("\n")
    
    def inicializa(self):                               #Método para evitar problemas com o numpy.
        for i in range (self.tam):                      #Percorre tabela.
            self.numeros[i] = -1                        #Inicializa posições.
    
    def busca(self, valor):
        encontrou = False

        for i in range(self.tam):
            if valor == self.numeros[i]:                #Verifica se o valor do usuário está na lista.
                encontrou = True
                break
        
        return encontrou


    def ordena(self):
        for i in range(1, self.tam):                    #Inicializa índice na segunda posição.
            for j in range(self.tam):                   #Inicializa o outro índice na primeira posição.
                if self.numeros[i] < self.numeros[j]:   #Verifica se o valor a frente é maior que o atual.
                    copia = self.numeros[i]             #Copia dados do menor.
                    self.numeros[i] = self.numeros[j]   #Troca o menor pelo maior.
                    self.numeros[j] = copia             #Coloca o maior na frente do menor.

#*********************************************************************************#
#*********************************************************************************#
#*********************************************************************************#

class Hash:

    def __init__(self, tam):
        self.tam = tam                                  #Define tamanho da lista.
        self.numeros = empty(self.tam, dtype=int)       #Inicializa a lista.
    
    def inicializa(self):                               #Método para evitar problemas com o numpy.
        for i in range (self.tam):                      #Percorre tabela.
            self.numeros[i] = -1                        #Inicializa posições.

    def indice(self, num):                              #Retorna resto da divisão.
        return int(num % 2500)                          #A divisão efetuada é: Chave / 1500.                    

    def mostra(self):
        for i in range(self.tam):                       #Percorre Tabela.
            if self.numeros[i] != -1:                   #Imprime valor válido.
                print(self.numeros[i], end=" ")         #Imprime os números em linha.
            else:                                       #Imprime '-' para valor inválido.
                print(" - ", end=" ")

            if (i % 10) == 0:                           #Quebra de linha a cada dez impressões.
                print("\n")

            if i > int(self.tam / 2) and self.numeros[i] == -1: #Se passou na última posição válida...
                break                                           #Encerra o método.
        print("\n")
    
    def insere(self):

        for i in range(int(self.tam / 2)):       #Laço para preencher Tabela.
            n = randint(0, 10000)                 #Gera número aleatório.
            ind = self.indice(n)                 #Calcula índice Hash do número.
            if self.numeros[ind] == -1:          #Se o índice está desocupado, insere nele.
                self.numeros[ind] = n
            
            elif self.numeros[ind] == n:         #Verifica se o valor já foi inserido.
                continue

            else:                                #Se estiver ocupado...
                for j in range(ind, self.tam):   #Procura próxima posição disponível.
                    if self.numeros[j] == -1:
                        self.numeros[j] = n
                        break
    
    def busca(self, num):

        ind = self.indice(num)                  #Calcula o Hash para encontrar o número.

        if self.numeros[ind] == num:            #Verifica se o número está na sua posição Hash.
            print("\nHash: O número {} está na posição {}".format(num, ind))
        
        elif self.numeros[ind+1] == -1:
            print("\nHash: Número não está na lista.")
        
        else:                                   #Se não estiver...
            for i in range(ind, self.tam):      #Inicia laço para buscar.
                if self.numeros[i] == -1:       #Se encontrou uma posição "inválida", encerra a busca.
                    print("\nHash: Número não está na lista.")
                    break
                    
                else:                           #Se a posição tem algum número válido...
                    if self.numeros[i] == num:  #Verifica se é o número buscado.
                        print("\nHash: O número {} está na posição {}".format(num, i))
                        break
        
#*********************************************************************************#
#*********************************************************************************#
#*********************************************************************************#

def entrada(min, max): #Função para validar a entrada.
    
    while True:                             #Laço para validar entrada.

        try:                                #Tenta pegar entrada.
            op = int(input("Digite uma opção: "))
    
        except ValueError:                  #Se a entrada não for um int...
            print("A entrada deve ser um valor inteiro.")

        else:                               #A entrada é um int...  
            if op >= min and op <= max:     #Verifica se é um valor válido.
                return op
            else:
                print("Escolha uma das opções exibidas.")

#*********************************************************************************#
#*********************************************************************************#
#*********************************************************************************#

def limpa(): #Função para limpar a tela.

    if name == "nt":                                 #Verifica se o sistema é Windows.
        system("cls")

    else:                                               #Se for outro Sistema Operacional.
        system("clear")

#*********************************************************************************#
#*********************************************************************************#
#*********************************************************************************#

def main(): #Função principal do programa.

    tabela = Hash(10000)                            #Cria a tabela Hash.
    tabela.inicializa()                             #Inicializa para evitar problema com o numpy.
    tabela.insere()                                 #Popula a Tabela Hash.

    lista = Seq(5000)                               #Cria a Lista Sequencial.
    lista.inicializa()                              #Inicializa para evitar problema com o numpy.
    lista.popula()                                  #Preenche a Lista Sequencial.
    lista.ordena()                                  #Ordena Lista Sequencial.

    while True:                                     #Laço do menu.

        print("---------------Menu---------------")
        print("0 - Sair")
        print("1 - Mostra a Lista Sequencial")
        print("2 - Mostra Tabela Hash")
        print("3 - Compara algoritmos de busca")
        print("4 - Limpa a tela\n")

        op = entrada(0, 4)                          #Armazena a opção do usuário.

        if op == 0:
            break                                   #Encerra o programa.

        elif op == 1:
            lista.mostra()                          #Método para mostrar Lista Sequencial.
        
        elif op == 2:
            tabela.mostra()                         #Método para mostrar Tabela Hash.
        
        elif op == 3:
            print("\nQual valor você deseja buscar na Lista Sequencial? ")
            op = entrada(0, 10000)                                  #Pega o número a ser pesquisado.

            print("\nQual valor deseja buscar na Tabela Hash? ")
            op2 = entrada(0, 10000)                                 #Pega o número a ser pesquisado.

            startBusca = process_time_ns()                         #Inicia a contagem de tempo.
            v = lista.busca(op)                                     #Chama método de busca Sequencial.
            endBusca = process_time_ns()                           #Termina a contagem de tempo.


            if v == False:                                          #Se o número não foi encontrado.
                print("\nSequencial: Valor não está na lista.")
            
            else:
                print("\nSequencial: O valor {} está na lista.".format(op))
            
            print("Tempo de busca Sequencial em nanosegundos: {}".format(endBusca - startBusca))

            startBusca = process_time_ns()                     #Inicia a contagem de tempo.
            tabela.busca(op2)                                   #Chama método de busca Hash.
            endBusca = process_time_ns()                       #Termina a contagem de tempo.
            
            
            print("Tempo de busca Hash em nanosegundos: {}".format(endBusca - startBusca))
            input("\n\nPressione enter para continuar...")

        else:
            limpa()                                              #Chama função para limpar a tela.

main()

#*********************************************************************************#
#*********************************************************************************#
#*********************************************************************************#