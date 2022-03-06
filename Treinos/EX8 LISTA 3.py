while True:
    num = int(input("Digite um número:"))
    if num == 0:
        break
    if num % 2 == 0:
        print("O número", num ,"é divisivel por 2.")
    if num % 3 == 0:
        print("O número", num ,"é divisivel por 3.")




# print("\nDetermina se N é perfeito.")

# n = int(input("\nDigite o valor de N: "))

# while True:
    
#     soma = 0
    
#     for divi in range(1,n):
#         if n % divi == 0:
#             soma += divi

#     if n == soma:
#         print("\nO numero {} é perfeito!".format(n))
#     else: 
#         print("\nO numero {} não é perfeito!".format(n))
    