def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num -1) + fibonacci(num -2)
        

entrada = int(input("Digite um número para calcular seu fibonacci: "))
x = 0

print(f'\n{20 * "="}\nRESULTADO:\n{20 * "="}')
while (x != entrada):
    res = fibonacci(x)
    print(res)
    x = x + 1
print(20 * "=" + "\n")
