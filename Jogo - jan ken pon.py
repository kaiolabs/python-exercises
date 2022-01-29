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

