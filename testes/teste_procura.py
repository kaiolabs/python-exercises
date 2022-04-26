string1 = '3'
file1 = open("dados.txt", "r") 
flag = 0
index = 0
for line in file1:   
    index += 1 
    if string1 in line: 
      flag = 1
      break 
          
if flag == 0:  
   print('String', string1 , 'Not Found')  
else:  
   print('String', string1, 'Found In Line', index) 
file1.close()  