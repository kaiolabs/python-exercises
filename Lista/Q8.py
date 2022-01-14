import os
contas = {}

while True:

    menu = int(input(f'\n{"="*40}\n{" "*18}MENU\n{"="*40}\n[ 1 ] - Criar uma conta.\n[ 2 ] - Atualiza saldo.\n[ 3 ] - Consulta saldo.\n[ 4 ] - Imprimr dados das contas.\n[ 0 ] - Sair\n{"="*40}\n\nInfome o número da opição desejada: '))

    if menu == 0:
        break

    if menu == 1:
        os.system('cls') or None
        nome = str(input("Informe o seu mome: "))
        rua = str(input("Informe a sua rua: "))

        while True:
            numeroConta = int(input("Informe o número da conta: "))
            if numeroConta in contas.keys():
                os.system('cls') or None
                print(f'{"="*60}\nJá existe uma conta com esse número informe outro número!\n{"="*60}\n')
            else:
                break

        CPF = int(input("Informe o seu CPF: "))
        tipoConta = int(input("[ 1 ] - Conta simples\n[ 2 ] - Conta especial\nInforme o número da opição de conta desejada: "))
        saldo = float(input("Informe o saldo da conta: "))
        contas[numeroConta] = [nome,rua,CPF,tipoConta,saldo,0]
        os.system('cls') or None

    if menu == 2:

        os.system('cls') or None
        menu2 = int(input("{}\n[ 1 ] - Adicionar dinheiro.\n[ 2 ] - Retirar dinheiro.\n{}\n\nInforme o número da opição desejada: ".format("="*40,"="*40)))

        if menu2 == 1:

            infoConta = int(input("Informe o número da conta: "))

            if infoConta in contas.keys():
                os.system('cls') or None
                addSaldo = float(input("Digite o valor que deseja adicionar: "))
                contas[infoConta][4] = contas[infoConta][4] + addSaldo
                os.system('cls') or None
                print("{}\nFoi adicionado R$ {} a sua conta!\n{}".format("="*40,addSaldo,"="*40))
            else:
                os.system('cls') or None
                print("{}\nConta inexistente!\n{}".format("="*40,"="*40))

        if menu2 == 2:

            infoConta = int(input("Informe o número da conta: "))

            if infoConta in contas.keys():
                os.system('cls') or None
                addSaldo = float(input("Digite o valor que deseja adicionar: "))
                if addSaldo < contas[infoConta][4]:
                    contas[infoConta][4] = contas[infoConta][4] - addSaldo
                    os.system('cls') or None
                    print("{}\nFoi retirado R$ {} a sua conta!\n{}".format("="*40,addSaldo,"="*40))
                    contas[infoConta][5] = contas[infoConta][5] + 1
                else:
                    os.system('cls') or None
                    print("{}\nVocê não tem saldo suficiente!\n{}".format("="*40,"="*40))

            else:
                os.system('cls') or None
                print("{}\nConta inexistente!\n{}".format("="*40,"="*40))

    if menu == 3:
        os.system('cls') or None
        infoConta = int(input("Informe o número da conta: "))
        if infoConta in contas.keys():
            os.system('cls') or None
            print("{}\nSeu saldo é de R$ {}\n{}".format("="*40,contas[infoConta][4], "="*40))
        else:
            os.system('cls') or None
            print("{}\nConta inexistente!\n{}".format("="*40,"="*40))
    
    if menu == 4:
        os.system('cls') or None
        for x in contas:

            chave = x

            valorNome = contas[chave][0]
            valorRua = contas[chave][1]
            valorCPF = contas[chave][2]
            valorTipoConta = contas[chave][3]

            if valorTipoConta == 1:
                tipo = "Simples"
            else:
                tipo = "Especial"

            valorSaldo = contas[chave][4]
            valorChequesDescontados = contas[chave][5]

            print(f'{"="*40}\nCONTA: {chave}\n{"="*40}\nNome: {valorNome}\nRua: {valorRua}\nCPF: {valorCPF}\nTipo da conta: {tipo}\nSaldo: {valorSaldo}\nForam descontados {valorChequesDescontados} cheques\n{"="*40}\n' )

