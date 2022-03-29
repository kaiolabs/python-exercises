def entradaDeDados ():
    dias = int(input("Informe o total de dias: "))
    return dias

def calculos():
    dias = entradaDeDados()
    anos = dias // 365
    dias = dias - anos*365
    meses = dias // 30
    dias = dias - meses*30
    dia = dias
    resultado(anos, meses, dia)

def resultado(a, m, d):
    print(f'\n{a} anos\n{m} meses\n{d} dias\n')

calculos()