import os
mediaLista = list()
n = 0

while True:
    if n < 0:
        break
    else:
        if len(mediaLista) == 5:
            mediaLista.pop(0)
            os.system('cls') or None
            mediaLista.append(n)
            mediaMovel = sum(mediaLista) / float(len(mediaLista))
            print("{}\n{}Média móvel\n{}\nA média móvel dos útimos 5 pontos foi: {}\n{}\nLista de pontos: {}\n{}".format("="*50, " "*19, "="*50, round(mediaMovel,2), "="*50, mediaLista, "="*50))
        else:
            mediaLista.append(n)

    n = float(input("Digite um número: "))