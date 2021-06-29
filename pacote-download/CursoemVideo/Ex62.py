n = int(input('Digite um numero: '))
r = int(input('Digite a razao: '))
cont = 0
total = 0
a = 10
while a !=0:
    total = total + a
    while cont < total:
        print('{} -> '.format(n), end='')
        n = n + r
        cont = cont + 1
    a = int(input('Quantos termos voce quer mostrar a mais? '))
    print('PAUSA')
print('Progressao finalizada com {} termos mostrados.'.format(cont))