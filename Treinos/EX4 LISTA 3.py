
a = float(input("\nDigite o primeiro termo:"))
r = float(input("Digite a razão:"))
termos = int(input("Informe quantos termos irá somar na PG: "))

TermosPG = [ a * r ** (x - 1) for x in range(1, termos + 1) ]
total = 0

for x in range(1, termos+1):
    pg = (a * r ** (x - 1))
    total = total + pg

print("\nOs primeiros termos são: {}".format(TermosPG))
print("\nO total da soma dos {} primeiros termos dessa PG é: {}\n".format(termos, total))
