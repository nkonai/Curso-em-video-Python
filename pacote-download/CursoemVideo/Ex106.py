from time import sleep
c = ('\033[m',    #0 - sem cores
     '\033[0;30;41m', # 1 - vermelho
     '\033[0;30;43m', # 2 - amarelo
     )

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'',1)
    help(com)
    sleep(2)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    print(c[0], end='')
    sleep(1)


comando = ''
while True:
    titulo('Sistema de ajuda PyHelp',1)
    comando = str(input('Funcao ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Ate logo!',2)