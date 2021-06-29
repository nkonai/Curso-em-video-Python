jogador = dict()
golslist = []
total = 0
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for i in range(0, partidas):
    gol = int(input(f'Quantos gols na partida {i}? '))
    golslist.append(gol)
    total +=gol
jogador['gols'] = golslist[:]
jogador['total'] = total
print(jogador)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i in range(0,partidas):
    print(f'Na partida {i}, fez {jogador["gols"][i]} gols. ')
print(f'Foi um total de {jogador["total"]} gols.')

