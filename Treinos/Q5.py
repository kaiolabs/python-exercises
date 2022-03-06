max = int(input("\nInforme o primeiro valor (max): "))
min = int(input("Informe o segundo valor (min): "))

if max < min:

    aux = max
    max = min
    min = aux

    print("\nOpa! Você digitou um valor para o (max) menor que o (min), então vou estar fazendo a troca dos valores, agora os valores ficarão assim:\n\nMAX: {}\nMIN: {}".format(max, min))
    print("\nValores inteiros divisíveis por 5 no intervalo de {} até {}.\n".format(min, max))
    for x in range(min, max+1):
        if x % 5 == 0:
            print("\t {}".format(x))

else:
    print("\nValores inteiros divisíveis por 5 no intervalo de {} até {}.\n".format(min, max))
    for x in range(min, max+1):
        if x % 5 == 0:
            print("\t {}".format(x))