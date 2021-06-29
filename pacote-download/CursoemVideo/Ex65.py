soma = 0
count = 0
maior = 0
menor = 0
r = 'Y'
while r=='Y':
    n = int(input('Digite um numero: '))
    if count == 0 or n > maior:
        maior = n
    if count == 0 or n < menor:
        menor = n
    soma = soma + n
    count = count + 1
    r = str(input('Quer continuar? [Y/N]: ')).upper().strip()
media = soma/count
print('A media e {:.2f}'.format(media))
print('O menor numero e {} e o maior numero e {}'.format(menor,maior))