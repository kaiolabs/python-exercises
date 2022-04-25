import modulos

quantidadeIOS = 0
quantidadeAPK = 0
somaIdade = 0

while True:

    try:
        idade = int(input("\nDigite sua idade: "))
        if (idade > 125 or idade <= 0):
            print("Idade invalida!")
            continue
    except ValueError:
        print("\nIdade invalida!")
        continue

    sistemaOperacional = modulos.Normalizador("Qual sistema operacional você usa (IOS ou ANDROID): ")

    if(sistemaOperacional == "IOS"):
        quantidadeIOS = quantidadeIOS + 1
        somaIdade = somaIdade + idade
    elif(sistemaOperacional == "ANDROID"):
        quantidadeAPK = quantidadeAPK + 1
        somaIdade = somaIdade + idade
    else:
        print("\nO sistema operacional informado está incorreto! Por favor prenha os dados novamente.\n")
        continue

    continuar = modulos.Normalizador("Deseja cadastrar mais dados (S/N): ")
    if(continuar == "N"):
        break

totalDePessoas = quantidadeIOS + quantidadeAPK
media = modulos.Media(somaIdade, totalDePessoas)

print("\n{}\n\nNúmero de entrevistados: {}\n\nTotal de usuários de IOS: {}\n\nTotal de usuários de ANDROID: {}\n\nIdade média dos entrevistados: {:.2f}\n\n{}\n\n".format(40*"=", totalDePessoas, quantidadeIOS, quantidadeAPK, media, 40*"="))