# numeroa primoa acima de 1000

for i in range(1000, 2000):
    primo = 0
    for j in range(2, i):
        if i % j == 0:
            primo = 1
    if primo == 0:
        print(i)