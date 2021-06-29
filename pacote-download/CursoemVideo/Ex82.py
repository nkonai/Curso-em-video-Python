list = []
par = []
impar = []
while True:
    numero = int(input('Digite um numero: '))
    list.append(numero)
    answer = input('Quer continuar? [S/N]: ')
    if answer in 'Nn':
        break
print(f'A lista completa e {list}')
for v in list:
    if v%2==0:
        par.append(v)
    else:
        impar.append(v)
print(f'A lista de pares e {par}')
print(f'A lista de imapres e {impar}')
