resultados = []

def entradaDeDados ():
    nTeste = int(input("Informe o número de casos de teste: "))
    return nTeste

def pilhaDeFigurinhas():

    t = entradaDeDados()
    for x in range(t):

        print(f'\nCaso {x+1}\n')
        entrada1 = int(input(f'Informe o 1° valor: '))
        entrada2 = int(input(f'Informe o 2° valor: '))

        resto = None
        while resto != 0:
            resto = entrada1 % entrada2
            entrada1 = entrada2
            entrada2 = resto
        resultados.append(entrada1)
    
    resultado()

def resultado():
    print(f'\n{20 * "="}\nRESULTADOS:\n{20 * "="}\n')
    for y in range(len(resultados)):
        print(f'Caso {y+1}: {resultados[y]}')
    print(f'\n{20 * "="}\n')


pilhaDeFigurinhas()
