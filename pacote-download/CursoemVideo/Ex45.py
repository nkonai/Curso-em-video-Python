import random
from time import sleep
jogador = str(input('Vamos jogar um jogo? Digite pedra, papel ou tesoura: '))
options = ['pedra','papel','tesoura']
pc = random.choice(options)
print('JO...')
sleep(1)
print('KEN...')
sleep(1)
print('PO!')
if jogador.lower()==pc:
    print('Ninguem ganhou. os dois escolheram {}'.format(pc))
elif jogador.lower()=='pedra':
        if pc=='papel':
            print('Eu ganhei, escolhi {} e voce escolheu {}'.format(pc, jogador.lower()))
        elif pc=='tesoura':
            print('Voce ganhou, escolheu {} e eu escolhi {}'.format(jogador.lower(), pc))

elif jogador.lower() == 'papel':
    if pc == 'tesoura':
        print('Eu ganhei, escolhi {} e voce escolheu {}'.format(pc, jogador.lower()))
    elif pc == 'pedra':
        print('Voce ganhou, escolheu {} e eu escolhi {}'.format(jogador.lower(), pc))
elif jogador.lower() == 'tesoura':
    if pc == 'pedra':
        print('Eu ganhei, escolhi {} e voce escolheu {}'.format(pc, jogador.lower()))
    elif pc == 'papel':
        print('Voce ganhou, escolheu {} e eu escolhi {}'.format(jogador.lower(), pc))
else:
    print('Opcao invalida')