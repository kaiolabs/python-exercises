from operator import index
import os

Reservas = [
    [False ,False ,False ,False ,False ,False ,False ,False],
    [False ,False ,False ,False ,False ,False ,False ,False],
    [False ,False ,False ,False ,False ,False ,False ,False],
    [False ,False ,False ,False ,False ,False ,False ,False],
    [False ,False ,False ,False ,False ,False ,False ,False],
    [False ,False ,False ,False ,False ,False ,False ,False],
    [False ,False ,False ,False ,False ,False ,False ,False],
    [False ,False ,False ,False ,False ,False ,False ,False],
    [False ,False ,False ,False ,False ,False ,False ,False],
    [False ,False ,False ,False ,False ,False ,False ,False]
]

contPosition = 0
contMesasLivres  = 0
contMesasOcupadas = 0

def cls():
    os.system('cls') or None

def linha(m):
    l = (m - 1)//8
    return l

def coluna(m):
    c = (m - 1)%8
    return c

def reserva_mesa(m):
    reserva_mesa = Reservas[linha(m)][coluna(m)] = True
    return reserva_mesa

def remover_reserva(m):
    reserva_mesa = Reservas[linha(m)][coluna(m)] = False
    return reserva_mesa


while True:
    op = int(input(f'\n------------- MENU -------------\n\n1 - Reservar mesa.\n2 - Cancelar reserva de mesa.\n3 - Lista de mesas livres\n4 - Apresentar os totalizadores\n0 - Sair\n{"-"*32}\n\nSelecione a opção desejada: '))

    if op == 0:
        break

    if op == 1:
        cls()
        mesa = int(input("Informe o número da mesa que deseja reserva: "))
        cls()

        if mesa > 80:
            cls()
            print(f'{"-"*32}\n\nSó temos 80 reservas!')
        
        elif Reservas[linha(mesa)][coluna(mesa)] == True:
            cls()
            print(f'{"-"*32}\n\nA mesa {mesa} já está reservada!')
            reserva_mesa(mesa)

        elif mesa > 0 and mesa <= 80:
            cls()
            reserva_mesa(mesa)
            print(f'{"-"*32}\n\nReserva feita com sucesso!')

    if op == 2:

        cls()
        mesa = int(input("Informe o número da mesa que deseja remover a reserva: "))
        remover_reserva(mesa)
        cls()
        print(f'{"-"*32}\n\nReserva removida com sucesso!')

    if op == 3:
        cls()
        while True:
            contPosition = 0
            print(f'{"="*65}\n{" "*11}Lista de identificadores das mesas livres\n{"="*65}\n')


            for l in range(0, 10):
                for c in range(0, 8):
                    if Reservas[l][c] == False:
                        contPosition = contPosition + 1
                        print(f'[{contPosition:^5}] ', end='')
                    else:
                        contPosition = contPosition + 1
                        print(f'[{"R":^5}] ', end='') #Mostra as mesas reservads com a letra R
                print()


            op = int(input(f'\n{"="*65}\n\nDigite 0 para voltar: '))

            if op == 0:
                cls()
                contPosition = 0
                break
    if op == 4:
        while True:
            cls()
            for l in range(0, 10):
                for c in range(0, 8):
                    if Reservas[l][c] == False:
                        contMesasLivres = contMesasLivres + 1
                    else:
                        contMesasOcupadas = contMesasOcupadas + 1
            
            print(f'\n{"="*30}\n{" "*8}Totalizadores\n{"="*30}\nHá {contMesasLivres} mesas livres.\nHá {contMesasOcupadas} mesas ocupadas.')

            op = int(input(f'{"="*30}\n\nDigite 0 para voltar: '))

            if op == 0:
                cls()
                contMesasOcupadas = contMesasLivres = 0
                break
