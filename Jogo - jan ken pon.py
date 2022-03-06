<<<<<<< HEAD
import random
import os

=======
>>>>>>> 84a473dc8103bc1fb2e3272e5c545c762dbdddd3
pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
<<<<<<< HEAD

=======
>>>>>>> 84a473dc8103bc1fb2e3272e5c545c762dbdddd3
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
<<<<<<< HEAD

=======
>>>>>>> 84a473dc8103bc1fb2e3272e5c545c762dbdddd3
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
<<<<<<< HEAD

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
=======
'''
#Pedra ganha da tesoura (amassando-a ou quebrando-a).
#Tesoura ganha do papel (cortando-o).
#Papel ganha da pedra (embrulhando-a).

import random

escolha_maquina = random.randint(1,3)
escolha_usuario = int(input("Vamos começar o jogo\n                        1-PEDRA, 2-PAPEL E 3-TESOURA.\nO que você escolhe? \n\n"))

if escolha_usuario == escolha_maquina:
  print("\nO JOGO EMPATOU!")
elif (escolha_usuario == 1 and escolha_maquina == 3) or (escolha_usuario == 2 and escolha_maquina == 1) or(escolha_usuario == 3 and escolha_maquina == 2):
     print("\nVOCÊ GANHOU!")
else:
  print("\nVOCÊ PERDEU!")

print("\n\n")
           #0       1       2
opcoes = [pedra , papel, tesoura]
print("Você:")
print(f"{opcoes[escolha_usuario -1 ]}\nMáquina:{opcoes[escolha_maquina -1 ]}")

>>>>>>> 84a473dc8103bc1fb2e3272e5c545c762dbdddd3
