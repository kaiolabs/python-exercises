while True:
    v = str(input("Digite um valor:"))
    if v == '':
        break
    else:
        if v in "1234567890":
            print("O valor ({}) é um número!".format(v))
        else:
            print("O valor ({}) não é um número!".format(v))