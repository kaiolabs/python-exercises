P = {"x": [0 , 0], "y": [0, 0]}

for x in range(0, 2):
    P["x"][x] = int(input("Digite o {}° ponto de X: ".format(x+1)))
    P["y"][x] = int(input("Digite o {}° ponto de Y: ".format(x+1)))

distancia =  float((P["x"][0] - P["x"][1])**2 + (P["x"][0] - P["x"][1])**2) ** 0.5

print("\n{}\nPontos: {}\n{}\nA distância entre os pontos é: {}\n{}\n".format("="*40, P, "="*40,round(distancia,2), "="*40))
