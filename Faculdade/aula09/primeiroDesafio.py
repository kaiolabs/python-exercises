import random

listaSorteio = [] 
frasesDoGame = ["Cagão", "Sortudo", "Você é a vergonha da profissão", "Pelo amor de Deus...", "Sem comentários..."]
frasesDaMain = ["\nQue resposta sem noção em meu amigo!", "\nValor muito baixo. Tente novamente", "\nValor muito alto. Tente novamente"]

def entradaDeDados(text):
  e = int(input(text))
  return e

def statusGame(tentativas):
    if(tentativas == 1 or tentativas == 0):
        resp = frasesDoGame[0]
    elif(tentativas >= 1 and tentativas <= 3):
        resp = frasesDoGame[1]
    elif(tentativas > 3 and tentativas <= 5):
        resp = frasesDoGame[2]
    elif(tentativas > 5 and tentativas <= 7):
        resp = frasesDoGame[3]
    elif(tentativas > 7):
        resp = frasesDoGame[4]
    return print(f'\nSTATUS DA PARTIDA: {resp}')

def main():
    print(f'\n{18 * "=="}\n\nBem vindo ao jogo de adivinhação!\n\n{18 * "=="}\n')

    cont = 0
    inicio = entradaDeDados("Informe um valor de inicio: ")
    fim = entradaDeDados("Informe um valor de fim: ")

    for i in range(1):
        listaSorteio.append(random.randint(inicio, fim))

    while True:
      resposta = entradaDeDados(f'\n{cont + 1}º tentativa: ')
      if(resposta > fim):
          print(frasesDaMain[0])
          cont = cont + 1
      elif(resposta < inicio):
          print(frasesDaMain[0])
          cont = cont + 1
      elif(resposta < inicio):
          print(frasesDaMain[1])
          cont = cont + 1
      elif(resposta<listaSorteio[0]):
        print(frasesDaMain[1])
        cont = cont + 1
      elif(resposta>listaSorteio[0]):
        print(frasesDaMain[2])
        cont = cont + 1
      elif(resposta==listaSorteio[0]):
        cont = cont + 1

        print(f'\n{18 * "=="}')
        print('Você acertou!')
        print(f'\n{cont} tentativas')
        print(f'\nPontuação: {1000 - cont * 50}')
        statusGame(cont)
        print(f'{18 * "=="}\n')
        break
    
main()