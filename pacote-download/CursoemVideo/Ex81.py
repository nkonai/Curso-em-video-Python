list = []
while True:
    numero = int(input('Digite um numero: '))
    list.append(numero)
    answer = input('Quer continuar? [S/N]: ').upper()
    if answer in 'Nn':
        break

print(f'Foram digitados {len(list)} numeros.')
print(f'A lista em ordem decrescente e {sorted(list,reverse=True)}')
if 5 in list:
    print('O numero 5 faz parte da lista')
else:
    print('O numero 5 nao faz parte da lista')