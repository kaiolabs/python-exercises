# A seguinte sequência de números 0 1 1 2 3 5 8 13 21... é conhecida como série de Fibonacci. Nessa sequência, 
# cada número, depois dos 2 primeiros, é igual à soma dos 2 anteriores. Escreva um algoritmo que leia um inteiro 
# N (N < 46) e mostre os N primeiros números dessa série.

# Entrada
# O arquivo de entrada contém um valor inteiro N (0 < N < 46).

# Saída
# Os valores devem ser mostrados na mesma linha, separados por um espaço em branco. Não deve haver espaço após o último valor.


def entradaDeDados ():
    a = int(input("\nDigite o valor:"))
    return a

def fibonacci ():
    x = 0
    dados = []
    entrada = entradaDeDados()

    while x < entrada:
        if x == 0 or x == 1:
            dados.append(x)
        if x > 1:
            aux = dados[x-2] + dados[x-1]
            dados.append(aux)
        x = x + 1
    for j in range(0, entrada):
        dados[j] = str(dados[j])

    resultado(dados, entrada)
  
def resultado(dados, entrada):
    valores = ' '.join(dados)
    print(f'\n{ (entrada * 3 ) * "="}\n {valores}\n{(entrada * 3 ) * "="}\n')


fibonacci()
