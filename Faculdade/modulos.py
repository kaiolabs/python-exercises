# Calcula a média

def Media(valor, quantidade):
    calculo = valor / quantidade
    return calculo

# Normaliza os dados de etrada para uma string(texto) em maiusculo.

def Normalizador(text):
    dadoNormalizado = str(input(text)).upper()
    return dadoNormalizado

# Mostra os resultados dentro de uma lista.

resultados = []
def Resultado():
    print('\n')
    for y in range(len(resultados)):
        print(resultados[y])
    print('\n')