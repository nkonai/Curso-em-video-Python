import random
from time import sleep
numero = random.randint(1,5)
guess = int(input('Escolha um numero entre 1 e 5:'))
print('Processando...')
sleep(2)
if guess==numero:
    print('Acertou!O numero era {}!'.format(numero))
else:
    print('Errou!O numero era {}, nao {}'.format(numero,guess))