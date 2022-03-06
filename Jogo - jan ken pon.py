import random
import os

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''



while True:

    escolhaMaquina = random.randint(1,3)
    escolhaUsuario = int(input("\n\nVamos começar o jogo\n\n1-PEDRA.\n2-PAPEL.\n3-TESOURA.\n\nEscolha uma opção: "))

    if escolhaUsuario == escolhaMaquina:
        os.system('cls')
        print("\nO JOGO EMPATOU!")
    elif (escolhaUsuario == 1 and escolhaMaquina == 3) or (escolhaUsuario == 2 and escolhaMaquina == 1) or(escolhaUsuario == 3 and escolhaMaquina == 2):
        os.system('cls')
        print("\nVOCÊ GANHOU!")
    elif(escolhaUsuario > 3):
        os.system('cls')
        print("\nOPÇÃO INVALIDA!")
        continue
    else:
        os.system('cls')
        print("\nVOCÊ PERDEU!")


    print("\n")
    opcoes = [pedra , papel, tesoura]
    print("Você:")
    print(f"{opcoes[escolhaUsuario -1 ]}\nMáquina:{opcoes[escolhaMaquina -1 ]}")

    continuar = str(input("Deseja continuar (S/N): ")).upper()

    if(continuar == "N"):
        break
    os.system('cls')
