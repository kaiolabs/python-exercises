dicionario = {"Campo 1": "String", "Campo 2": (0, 0, 0)}

print("\n{}\n {}Dicionário inicial\n{}".format("="*50, " "*15, "="*50))

for z in dicionario:
    chave = z
    valor = dicionario[z]
    print("| {} | {} |".format(chave, valor))
print("="*50)

s = str(input("\nDigite uma string: "))
dicionario["Campo 1"] = s

for x in range(0, 3):
        n = int(input("Digite o {}° valor: ".format(x+1)))
        y = list(dicionario["Campo 2"])
        y[x] = n
        dicionario["Campo 2"] = tuple(y)

print("\n{}\n {}Dicionário final\n{}".format("="*50, " "*15, "="*50))
for z in dicionario:
    chave = z
    valor = dicionario[z]
    print("| {} | {} |".format(chave, valor))
print("="*50,"\n")
