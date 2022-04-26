file = open("dados.txt","r") 

def tamanhoMax():
     Counter = 0
     Content = file.read() 
     CoList = Content.split("\n") 
          
     for i in CoList: 
          if i: 
               Counter += 1
                         
     return Counter

print(tamanhoMax())