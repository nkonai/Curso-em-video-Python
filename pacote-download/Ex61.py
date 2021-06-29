n = int(input('Digite um numero: '))
r = int(input('Digite a razao: '))
cont = 0
while cont<10:
    print('{} -> '.format(n),end='')
    n = n + r
    cont = cont + 1