# Leia 2 valores inteiros e armazene-os nas variáveis A e B. Efetue a soma de A e B 
# atribuindo o seu resultado na variável X. Imprima X conforme exemplo apresentado 
# abaixo. Não apresente mensagem alguma além daquilo que está sendo especificado e não 
# esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".

def entradaDeDados ():
    a = int(input(" 1° valor: "))
    b = int(input(" 2° valor: "))
    return a, b

def somaValores():
    a, b = entradaDeDados()
    soma = a + b
    resultado(a, b, soma)

def resultado(a, b, soma):
    print(f'\nA soma entre {a} e {b} é: {soma}\n')

somaValores()