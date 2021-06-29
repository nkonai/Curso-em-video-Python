while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n >=0:
        for cont in range(1,11):
            print('{} X {} = {}'.format(n,cont,n*cont))
    else:
        break
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')