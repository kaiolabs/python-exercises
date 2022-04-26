import random

valoresNaoOrdenados = [random.randrange(0, 999999) for i in range(0, 999999)]

def remove_duplicates(lista):
    novaLista = []
    for i in range(len(lista)):
        if lista[i] not in novaLista:
            novaLista.append(lista[i])
    return novaLista

print(remove_duplicates(valoresNaoOrdenados))
