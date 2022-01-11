import os
A = list()
POS = list()
NEG = list()

n = int(input("Digite um valor entre (0 e 50): "))

while True:

    if (n <= 50) and (n >= 0):
        
        r = float(input("Insira um número, para parar digite (999): "))

        if r == 999:
            break
        else:
            A.append(r)

    else:
        os.system('cls') or None
        print("Você não digite um valor entre (0 e 50)!")
        n = int(input("\nPor favor digite um valor entre (0 e 50): "))

os.system('cls') or None
for x in A:
    if x >= 0:
        POS.append(x)
    else:
        NEG.append(x)

print("{}{}\nA lista total é: {}".format("="*60, "\t", A))
print("{}{}A lista dos valores positivos é: {}".format("="*60, "\n", POS))
print("{}{}A lista dos valores negativos é: {}\n{}".format("="*60, "\n", NEG, "="*60))
