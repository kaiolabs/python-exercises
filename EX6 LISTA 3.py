n = int(input("\nDigite um valor inteiro:"))
x = str
maior = menor = quant = 0

while x != "N":

   n2 = float(input("Digite um valor real:"))
   quant += 1

   if quant == 1:
      maior = menor = n2
   else:
      if n2 > maior:
         maior = n2
      if n2 < menor:
         menor = n2
   
   x = str(input("Quer continuar (S/N): ")).upper()


print("\nO número inteiro foi: {}".format(n))
print("\nVocê digitou {} números REAIS.".format(quant))
print("\nO maior entre os número REAIS foi: {}".format(maior))
print("\nO menor entre os número REAIS foi: {}\n".format(menor))
   
