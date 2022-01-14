dicionarioNumeros = dict()

while True:
    
    numEntrada = int(input("Digite um número:"))

    if numEntrada <= 0:
        break
    else:
        if numEntrada in dicionarioNumeros.keys():
            dicionarioNumeros[numEntrada].append(1)
        else:
            dicionarioNumeros[numEntrada] = [1]

print("="*50)
for x, y in dicionarioNumeros.items():
    chave = x
    valor = sum(y)
    print("O número {} se repete {} vezes.".format(chave, valor))
print("="*50)