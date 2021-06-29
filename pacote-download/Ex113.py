def leiaint(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Por favor digite um numero inteiro valido.\033[m')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida')
            return 0
        else:
            return num


def leiafloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Por favor digite um numero real valido.\033[m')
            continue
        else:
            return num


n = leiaint('Digite um numero inteiro: ')
f = leiafloat('Digite um numero real: ')
print(f'Voce acabou de digitar o numero {n} e {f}.')
