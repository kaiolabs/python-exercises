def imprimir(self):
        if self.utimaPosicao == -1:
            print("O vetor está vazio")
        else:
            for i in range(self.utimaPosicao + 1):
                print(i, ' - ' , self.valores[i])


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