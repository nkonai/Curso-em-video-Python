contidade = 0
nhomens = 0
nmulheres = 0
while True:
    print('CADASTRE UMA PESSOA')
    idade = int(input('Idade: '))
    sexo = ' '
    choice = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]: ')).upper().strip()[0]
    while choice not in 'SN':
        choice = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if idade >=18:
        contidade += 1
    if sexo =='M':
        nhomens += 1
    if idade <=20 and sexo =='F':
        nmulheres += 1
    if choice =='N':
        break
print('''
Total de pessoas com mais de 18 anos: {}
Ao todo temos {} homens cadastrados
E temos {} mulheres com menos de 20 anos'''.format(contidade,nhomens,nmulheres))
