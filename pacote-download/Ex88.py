import random
from time import sleep
jogos = int(input('Quantos jogos voce quer que eu sorteie? '))
for j in range(1,jogos+1):
    list = []
    cont = 0
    while True:
        numero = random.randint(0,60)
        if numero not in list:
            list.append(numero)
            cont += 1
        if cont >=6:
            break
    print(f'Jogo {j}: {list}')
    sleep(1)
    list.clear()