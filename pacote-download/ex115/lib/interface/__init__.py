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


def linha(tam=30):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(30))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - \033[1;34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('Sua opcao: ')
    return opc


