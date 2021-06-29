from random import randint
from time import sleep

def sorteia(lst):
    print('Sorteando 5 valores da lista:',end=' ')
    for i in range(0,5):
        n = randint(0,10)
        print(n, end=' ')
        lst.append(n)
        sleep(0.3)
    print('PRONTO!')

def somapar(lst):
    print(f'Somando os valores pares de {lst}, temos',end=' ')
    soma = 0
    for n in lst:
        if n % 2 == 0:
            soma += n
    print(soma)

numeros = list()
sorteia(numeros)
somapar(numeros)