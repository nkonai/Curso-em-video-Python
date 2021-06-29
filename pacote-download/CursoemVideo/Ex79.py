list = []
answer ='S'
while answer =='S':
    numero = int(input('Digite um valor: '))
    if numero in list:
        print('Valor duplicado!Nao vou adicionar!')
    else:
        list.append(numero)
    answer = str(input('Quer continuar? [S/N]: ')).upper()
print(f'Voce digitou os valores {sorted(list)}')
