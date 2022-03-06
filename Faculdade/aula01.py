quantidadeIOS = 0
quantidadeAPK = 0
somaIdade = 0

while True:

    idade = int(input("\nDigite sua idade: "))
    sistemaOperacional = str(input("Qual sistema operacional você usa (IOS ou ANDROID): ")).upper()

    if(sistemaOperacional == "IOS"):
        quantidadeIOS = quantidadeIOS + 1
        somaIdade = somaIdade + idade
    elif(sistemaOperacional == "ANDROID"):
        quantidadeAPK = quantidadeAPK + 1
        somaIdade = somaIdade + idade
    else:
        print("\nO sistema operacional informado está incorreto! Por favor prenha os dados novamente.\n")
        continue

    continuar = str(input("Deseja cadastrar mais dados (S/N): ")).upper()

    if(continuar == "N"):
        break

totalDePessoas = quantidadeIOS + quantidadeAPK
media = somaIdade / totalDePessoas

print("\n{}\n\nNúmero de entrevistados: {}\n\nTotal de usuários de IOS: {}\n\nTotal de usuários de ANDROID: {}\n\nIdade média dos entrevistados: {}\n\n{}\n\n".format(40*"=", totalDePessoas, quantidadeIOS, quantidadeAPK, media, 40*"="))