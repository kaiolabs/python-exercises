def primo(n):

    divi=0
    
    for x in range(1,n+1):
        if n % x == 0:
            divi += 1

    if divi==2:
        return True
    else:
        return False
        
def exibe():
    
    n = int(input("\nExibir números primos até: "))
    
    for x in range(1,n+1):
        if(primo(x)):
            print("O número {} é primo!".format(x))
    
while True:
    exibe()


