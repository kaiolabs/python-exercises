# João quer montar um painel de leds contendo diversos números. Ele não possui muitos leds, e não tem certeza 
# se conseguirá montar o número desejado. Considerando a configuração dos leds dos números abaixo, faça um 
# algoritmo que ajude João a descobrir a quantidade de leds necessário para montar o valor.

# Entrada
# A entrada contém um inteiro N, (1 ≤ N ≤ 1000) correspondente ao número de casos de teste, seguido de N linhas, 
# cada linha contendo um número (1 ≤ V ≤ 10100) correspondente ao valor que João quer montar com os leds.

# Saída
# Para cada caso de teste, imprima uma linha contendo o número de leds que João precisa para montar o valor desejado, 
# seguido da palavra "leds".


qLeds = []

# Responsavel pela entrada de dados
def entradaDeDados ():
    nTeste = int(input("Informe o número de casos de teste: "))
    return nTeste


# Exibir resultados
def resultado():
    print('\n')
    for y in range(len(qLeds)):
        print(f'{y+1}° valor: {qLeds[y]} leds')
    print('\n')


# Função principal
def main():
    
    t = entradaDeDados()
    contador = 0

    for x in range(t):
        valores = (input(f'Informe o {x+1}° valor: '))
        for i in valores:

            if (i == '0' or i == '6' or i == '9'):
                contador = contador + 6
            elif (i == '2' or i == '3' or i == '5'):
                contador = contador + 5
            elif (i == '1'):
                contador = contador + 2
            elif (i == '4'):
                contador = contador + 4
            elif (i == '7'):
                contador = contador + 3
            elif (i == '8'):
                contador = contador + 7

        qLeds.append(contador)
        contador = 0

    resultado()


# Chamando a função principal
main()