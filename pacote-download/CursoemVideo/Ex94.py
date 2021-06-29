lista = []
pessoa = dict()
continuar = 'S'
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo:[M/F]  ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO!')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    lista.append(pessoa.copy())

    while True:
        continuar = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if continuar in 'SN':
            break
        print('ERRO!')
    if continuar =='N':
        break
print('-='*30)
print(f'Ao todo temos {len(lista)} pessoas cadastradas')
media = soma/ len(lista)
print(f'A media de idade e de {media:5.2f} anos')
print(f'As mulheres cadastradas foram ', end='')
for p in lista:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('Lista das pessoas que estao acima da media: ')
for p in lista:
    if p['idade']>=media:
        print(' ')
        for k,v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
