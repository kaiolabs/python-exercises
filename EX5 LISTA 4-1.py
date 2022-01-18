def verificar_texto(texto, string):
    if string in texto:
        print(f'{"="*60}\nA string contém na palavra\nA ultima ocrrencia de string na frase é na posição {texto.rfind(string)+1}º\n{"="*60}')
    else:
        print(f'{"="*50}\nA letra não contém na palavra!\n{"="*50}')

t = str(input("Digite o texto:"))
c = str(input("Digite uma string a ser pesquisada dentro do texto:"))
s = verificar_texto(t,c)