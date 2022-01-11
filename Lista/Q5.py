L = list()
res = ""
while True:

    if res == "N":
        break
    else:
        P = {"x": [0 , 0], "y": [0, 0]}
        for x in range(0, 2):
            P["x"][x] = int(input("Digite o {}° ponto de X: ".format(x+1)))
            P["y"][x] = int(input("Digite o {}° ponto de Y: ".format(x+1)))
            
        distancia =  float((P["x"][0] - P["x"][1])**2 + (P["x"][0] - P["x"][1])**2) ** 0.5
        L.append(round(distancia,2))

        res = str(input("Deseja continuar [S/N]")).upper()

print("\n{}\n\nLista de pontos: {}\n\n{}".format("="*50, L, "="*50))
