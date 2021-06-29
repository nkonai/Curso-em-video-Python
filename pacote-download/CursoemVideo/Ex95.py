lista = []
jogador = dict()
golslist = []
total = 0

while True:
    jogador.clear()
    golslist.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for i in range(0, jogador['partidas']):
        gol = int(input(f'Quantos gols na partida {i}? '))
        golslist.append(gol)
        total += gol
    jogador['gols'] = golslist[:]
    jogador['total'] = total
    lista.append(jogador.copy())
    continuar = str(input('Quer continuar? [S/N] '))
    if continuar in 'Nn':
        break

print('-='*20)
for i in jogador.keys():
    print(f'{i:<12}', end='')
print()
print('-'*40)
for k, v in enumerate(lista):
    print(f'{k:<4} ', end='')
    for d in v.values():
        print(f'{str(d):<10}', end='')
    print()

while True:
    a = int(input('Mostrar dados de qual jogador? '))
    if a == 999:
        print('<< VOLTE SEMPRE >>')
        break
    elif a >= len(lista):
        print('ERRO, digite um numero valido')
    else:
        print(f'--LEVANTAMENTO DO JOGADOR {lista[a]["nome"]}.')
        for p in range(0, lista[a]['partidas']):
            print(f'No jogo {p} fez {lista[a]["gols"][p]} gols.')
        print('-'*30)


