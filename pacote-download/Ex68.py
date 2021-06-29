import random
c = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = random.randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou impar? [P/I]: ')).upper().strip()[0]
    print('Voce jogou {} e o computador jogou {}. Total de {}'.format(jogador, computador, total))
    print('DEU PAR' if total%2 == 0 else 'DEU IMPAR!')
    if tipo == 'P':
        if total%2 == 0:
            print('Voce venceu!')
            c += 1
        else:
            break
    elif tipo == 'I':
        if total%2 == 1:
            print('Voce venceu!')
            c += 1
        else:
            break
    print('Vamos jogar novamente!')
print(f'GAME OVER! Voce venceu {c} vezes.')
