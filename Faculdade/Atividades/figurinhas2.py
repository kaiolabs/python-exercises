#Armazena os resultados
resultados = []

#Parte responsavel por ler o número de casos de teste
def entradaDeDados ():
    nTeste = int(input("Informe o número de casos de teste: "))
    return nTeste

#Parte que calcula o máximo divisor comum de dois inteiros
def recursividadeMDC(e1, e2):
    #A recursividade é interrompida quando e2 for igual a 0
    if(e2 == 0):
        return e1
    else:
        #Faz uma nova chamada a função recursividadeMDC
        return recursividadeMDC(e2, e1 % e2)

#Parte que mostra os resultados
def resultado():
    print(f'\n{20 * "="}\nRESULTADOS:\n{20 * "="}\n')
    for y in range(len(resultados)):
        print(f'Caso {y+1}: {resultados[y]}')
    print(f'\n{20 * "="}\n')

#Parte que executa o programa
def main():
    e = entradaDeDados()
    for x in range(e):
        print(f'\nCaso {x+1}\n')
        entrada1 = int(input(f'Informe o 1° valor: '))
        entrada2 = int(input(f'Informe o 2° valor: '))

        r = recursividadeMDC(entrada1, entrada2)
        resultados.append(r)

    resultado()

#Chama a função main
main()
    