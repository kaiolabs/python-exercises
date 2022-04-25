import random
with open("dados.txt", "w") as dados:
    for i in range(10):
        # Insere valores aleatórios.
        A = (random.randrange(0, 10))  # Gera um número randômico em uma faixa, entre 0 e 999.
        # verificar se o valor já existe no arquivo
        
        dados.write(str(A) + "\n")
        
# dados.close()

# criar valores aleatorios e salva no arquivo dados.txt
# import random
# with open("dados.txt", "w") as dados:
#     for i in range(10):
#         # Insere valores aleatórios.
#         A = (random.randrange(0, 10))  # Gera um número randômico em uma faixa, entre 0 e 999.
#         # verificar se o valor já existe no arquivo

for i in range(100):
    if __name__ == '__main__':
        # Insere valores aleatórios.
        A = (random.randrange(0, 10))  # Gera um número randômico em uma faixa, entre 0 e 999.
        # verificar se o valor já existe no arquivo
        with open("dados.txt", "w") as dados:
            dados.write(str(A) + "\n")
        dados.close()
