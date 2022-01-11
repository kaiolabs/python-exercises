a = float(input("\nDigite o primeiro termo:"))
r = float(input("Digite a razão:"))
termos = int(input("Informe a quantidade de termos da PA: "))

TermosPA = list()
TermosPA = [(a + (x - 1) * r) for x in range(1, termos + 1)]

print("\nOs {} primeiros termos são: {}\n".format(termos, TermosPA))