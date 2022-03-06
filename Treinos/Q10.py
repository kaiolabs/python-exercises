def perfeito(n):

    soma=0

    for x in range(1,n):
        if n % x == 0:
            soma += x

    if soma==n:
        return True
    else:
        return False
        
def exibe():
    
    n = int(input("\nExibir perfeitos até o número: "))
    
    for x in range(1,n+1):
        if(perfeito(x)):
            print("O número {} é perfeito!".format(x))
    
while True:
    exibe()


