dicionario = dict()

while True:

    nome = input('Qual o nome do contato?:')
    
    if nome == '':
        break

    idade = int(input('Qual a idade?:'))
    tel = int(input('Qual o telefone do contato:?'))
    dicionario[nome] = (idade, tel)

print("\n{}\n{}Lista telefonica{}{}{}".format("="*45," "*14, "\n", "="*45, ""))
for dic in sorted(dicionario):
    chave = dic
    valor = dicionario[dic]
    print("| {} | {} |".format(chave, valor,))
print("="*45)

menores18 = dict()
maiores18 = dict()

for x, y in dicionario.items():

    if y[0] < 18:
        menores18[x] = y
    else:
        maiores18[x] = y

del dicionario

print("\n{}\n{}Maiores de 18{}{}{}".format("="*45," "*14, "\n", "="*45, ""))
for dic in sorted(maiores18):
    chave = dic
    valor = maiores18[dic]
    print("| {} {} ".format(chave, valor,))
print("="*45)

print("\n{}\n{}Menores de 18{}{}{}".format("="*45," "*14, "\n", "="*45, ""))
for dic in sorted(menores18):
    chave = dic
    valor = menores18[dic]
    print("| {} {} ".format(chave, valor,))
print("="*45)
print("\n\n")