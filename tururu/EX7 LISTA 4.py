AA=[]
A=[]
max = int(input("\nInforme o primeiro valor (max): "))
min = int(input("Informe o segundo valor (min): "))
if max < min:

    aux = max
    max = min
    min = aux
    print("\nOpa! Você digitou um valor para o (max) menor que o (min), então vou estar fazendo a troca dos valores, agora os valores agora os valores ficarão assim:\n\nMAX: {}\nMIN: {}".format(max, min))
    for x in range(min, max + 1):
        if x % 7 == 0:
            AA.append(x)
            print("Os valores são: {}".format(AA))
else:
    print("\nValores inteiros divisíveis por 7 no intervalo de {} até {}.\n".format(min, max))
    for i in range(min, max + 1) :
        if i % 7 == 0:
            A.append(i)

print("Os valores são: {}\n".format(A))