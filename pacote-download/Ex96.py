def area(b,c):
    a = b*c
    print(f'A area de um terreno {b} X {c} e de {a}m2.')


print('Controle de Terrenos')
print('-'*30)
lar = float(input('LARGURA (m): '))
com = float(input('COMPRIMENTO (m): '))

area(lar,com)