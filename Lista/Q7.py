import os

relatorioGeral = {"Segunda": [], "Terça": [], "Quarta": [], "Quinta": [], "Sexta": [], "Sábado": [], "Domingo": []}
produtos = {}
media = 0

while True:
    os.system('cls') or None
    print("{}\n{}Registro de produtos\n{}".format("="*50," "*14,"="*50))
    dia = int(input(f"\n[ 1 ] - Segunda-feira.\n[ 2 ] - Terça-feira.\n[ 3 ] - Quarta-feira.\n[ 4 ] - Quinta-feira.\n[ 5 ] - Sexta-feira.\n[ 6 ] - Sábado.\n[ 7 ] - Domingo.\n\nDigite o número do dia que deseja cadastra o produto: "))

    os.system('cls') or None
    cod = (int(input("Informe o código do produto: ")))
    tipo = (str(input("Informe o tipos disponível [P - M - G]: ")))
    quantidade = (int(input("Informe a quantidade vendida: ")))
    res = str(input("Deseja cadastra mais um produto [S/N]: "))

    if dia == 1:
        relatorioGeral["Segunda"].append(quantidade)
    if dia == 2:
        relatorioGeral["Terça"].append(quantidade)
    if dia == 3:
        relatorioGeral["Quarta"].append(quantidade)
    if dia == 4:
        relatorioGeral["Quinta"].append(quantidade)
    if dia == 5:
        relatorioGeral["Sexta"].append(quantidade)
    if dia == 6:
        relatorioGeral["Sábado"].append(quantidade)
    if dia == 5:
        relatorioGeral["Domingo"].append(quantidade)

    if cod in produtos.keys():
        produtos[cod].append(quantidade)
    else:
        produtos[cod] = [quantidade]

    if res in "Nn":
        break
    
os.system('cls') or None
print("{}\n{}Total vendido em cada dia\n{}".format("="*50," "*12,"="*50,))
for x, y in relatorioGeral.items():
    chave = x
    valor = sum(y)
    print("{}: {}".format(chave, valor))
    media = media + sum(y) / 7
print("="*50)
print("\n{}\n{}Média da semana\n{}\nMÉDIA: {}\n{}\n".format("="*50," "*15,"="*50,round(media, 2),"="*50))
print("{}\n{}Total vendido de cada produto\n{}".format("="*50," "*10,"="*50,))
for x, y in produtos.items():
    chave = x
    valor = sum(y)
    print("Foi vendido ( {} ) unidades do produto ( {} )".format(valor, chave))
print("="*50)

print("\n")
print(produtos)
print(relatorioGeral)
print("\n")