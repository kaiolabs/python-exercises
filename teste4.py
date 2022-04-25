lista = []

for i in range(100):
    lista.append(random.randrange(0, 100))   

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