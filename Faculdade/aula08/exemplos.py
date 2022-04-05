import os

class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def mostrar_no(self):
        print(self.valor)
        
#========================================================#

class ListaEncadeada:

    def __init__(self):
        self.primeiro = None

    def inserir_inicio(self, valor):
        novo = No(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo

    def inserir_fim(self, valor):
        novo = No(valor)
        if self.primeiro == None:
            self.primeiro = novo
        else:
            no = self.primeiro
            while no.proximo != None:
                no = no.proximo
            no.proximo = novo

    def inserir_posicao(self, posicao, valor):
        novo = No(valor)
        if posicao == 1:
            novo.proximo = self.primeiro
            self.primeiro = novo
        else:
            no = self.primeiro
            i = 1
            while no.proximo != None and i < posicao:
                no = no.proximo
                i += 1
            novo.proximo = no.proximo
            no.proximo = novo

    def remover_inicio(self):
        if self.primeiro != None:
            self.primeiro = self.primeiro.proximo
            self.primeiro = None

    def remover_fim(self):
        if self.primeiro != None:
            no = self.primeiro
            while no.proximo.proximo != None:
                no = no.proximo
            no.proximo = None

    def remover_posicao(self, posicao):
        if posicao == 1:
            self.primeiro = self.primeiro.proximo
            self.primeiro = None
        else:
            no = self.primeiro
            i = 1
            while no.proximo != None and i < posicao:
                no = no.proximo
                i += 1
            no.proximo = no.proximo.proximo
            no.proximo = None

    def mostra_lista(self):
        if self.primeiro == None:
            print("Lista vazia")
        else:
            no = self.primeiro
            while no != None:
                no.mostrar_no()
                no = no.proximo
    

    def tamanho(self):
        if self.primeiro == None:
            return 0
        else:
            no = self.primeiro
            i = 0
            while no.proximo != None:
                no = no.proximo
                i += 1
            return i

    def pesquisar(self, valor):
        if self.primeiro == None:
            print("Lista vazia")
        else:
            no = self.primeiro
            i = 0
            while no != None:
                if no.valor == valor:
                    os.system('cls') or None
                    print(f'{20 * "=="}\nO valor {valor} foi encontrado na posição {i}\n{20 * "=="}')
                    return
                no = no.proximo
                i += 1
            os.system('cls') or None
            print(f'{20 * "=="}\nO valor {valor} não foi encontrado\n{20 * "=="}')
    

    
    
#========================================================#

lista = ListaEncadeada()

lista.inserir_inicio(1)
lista.inserir_inicio(2)
lista.inserir_inicio(3)

while True:
    print("\n1 - Inserir no inicio\n2 - Inserir no fim\n3 - Inserir na posicao\n4 - Remover no inicio\n5 - Remover no fim\n6 - Remover na posicao\n7 - Mostra lista lista\n8 - Tamanho da lista\n9 - Busca valor\n10 - Sair")

    opcao = int(input("\nInforme a opção: "))

    if opcao == 1:
        valor = int(input("Digite o valor: "))
        lista.inserir_inicio(valor)
        os.system('cls') or None

    elif opcao == 2:
        valor = int(input("Digite o valor: "))
        lista.inserir_fim(valor)
        os.system('cls') or None

    elif opcao == 3:
        posicao = int(input("Digite a posicao: "))
        valor = int(input("Digite o valor: "))
        lista.inserir_posicao(posicao, valor)
        os.system('cls') or None

    elif opcao == 4:
        lista.remover_inicio()
        os.system('cls') or None

    elif opcao == 5:
        lista.remover_fim()
        os.system('cls') or None

    elif opcao == 6:
        posicao = int(input("Digite a posicao: "))
        lista.remover_posicao(posicao)
        os.system('cls') or None

    elif opcao == 7:
        os.system('cls') or None
        print("========LISTA========")
        lista.mostra_lista()
        print("=====================")

    elif opcao == 8:
        os.system('cls') or None
        print("=====================")
        print(lista.tamanho())
        print("=====================")
        
    elif opcao == 9:
        lista.pesquisar(int(input("Digite o valor: ")))
    elif opcao == 10:
        break
    else:
        print("Opção invalida")
