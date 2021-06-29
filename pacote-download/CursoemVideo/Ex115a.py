
print('-'*30)
print('MENU PRINCIPAL'.center(30))
print('-'*30)
print('\033[1;33m1\033[m - \033[1;34mVer pessoas cadastradas\033[m')
print('\033[1;33m2\033[m - \033[1;34mCadastrar nova pessoa\033[m')
print('\033[1;33m3\033[m - \033[1;34mSair do sistema\033[m')
print('-'*30)

def leiaopcao(msg):
    while True:
        try:
            opcao = int(input(msg))
            while opcao > 3 or opcao < 1:
                print('ERRO! Digite uma opcao valida: ')
                opcao = int(input(msg))
            if opcao == 1:
                print('-' * 30)
                print('OPCAO 1'.center(30))
                print('-' * 30)
            elif opcao == 2:
                print('-' * 30)
                print('OPCAO 2'.center(30))
                print('-' * 30)
            else:
                print('-' * 30)
                print('Saindo do sistema...Ate logo!'.center(30))
                print('-' * 30)
                break
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite uma opcao valida: \033[m')
            continue
        else:
            return opcao

n = leiaopcao('\033[1;33mSua opcao: \033[m')
