import numpy as np


class vetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.utimaPosicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def imprimir(self):
        if self.utimaPosicao == -1:
            print("O vetor está vazio")
        else:
            for i in range(self.utimaPosicao + 1):
                print(i, ' - ', self.valores[i])

    def inserir(self, valor):
        if self.utimaPosicao == self.capacidade - 1:
            print("O vetor está cheio")
        else:
            self.utimaPosicao += 1
            self.valores[self.utimaPosicao] = valor

    def pesquisar(self, valor):
        if self.utimaPosicao == -1:
            print("O vetor está vazio")
        else:
            for i in range(self.utimaPosicao + 1):
                if self.valores[i] == valor:
                    print("O valor", valor, "foi encontrado na posição", i)
                    return
            print("O valor", valor, "não foi encontrado")

    def remover(self, valor):
        if self.utimaPosicao == -1:
            print("O vetor está vazio")
        else:
            for i in range(self.utimaPosicao + 1):
                if self.valores[i] == valor:
                    self.valores[i] = self.valores[self.utimaPosicao]
                    self.utimaPosicao -= 1
                    print("O valor", valor, "foi removido")
                    return
            print("O valor", valor, "não foi encontrado")

    # Buscar binária por um valor.

    def busca_binaria(self, valor):
        inicio = 0
        fim = self.ultimaPosicao
        while inicio <= fim:
            meio = int((fim + inicio) / 2)  # Encontra a posição do meio.
        if self.valores[meio] == valor:
            return meio
        # Se valor menor do que o valor que está no meio, reposiciona o marcador do fim.
        elif valor < self.valores[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1
        return -1


vetor = vetorNaoOrdenado(5)

vetor.inserir('kaio')
vetor.inserir(2)
vetor.inserir(3)
vetor.inserir(4)
vetor.inserir(5)

vetor.imprimir()

vetor.pesquisar(2)

vetor.remover(2)

vetor.imprimir()

