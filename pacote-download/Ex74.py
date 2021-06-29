from random import randint

numeros = (randint(0,10),randint(0,10),
     randint(0, 10),randint(0,10),
     randint(0, 10))
for n in numeros:
    print(f'{n} ', end='')
print('\nO maior numero sorteado e {}.'.format(max(numeros)))
print('O menor numero sorteado e {}.'.format(min(numeros)))


