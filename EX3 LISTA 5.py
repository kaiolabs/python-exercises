f = str(input("Digite uma frase:"))
l = str(input("Digite uma letra:"))
if l in f:
    print(f'{"="*60}\nA letra contém na palavra\nA ultima ocrrencia de caractere na frase é na posição {f.rfind(l)+1}º\n{"="*60}')
else:
    print(f'{"="*50}\nA letra não contém na palavra!\n{"="*50}')