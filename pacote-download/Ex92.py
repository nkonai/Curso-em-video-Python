from datetime import date
pessoa = dict()

pessoa['nome'] = str(input('Nome: '))
pessoa['idade'] = date.today().year - int(input('Ano de nascimento: '))
pessoa['ctps'] = int(input('Carteira de trabalho (0 nao tem): '))
while True:
    if pessoa['ctps'] == 0:
        break
    else:
        pessoa['contratacao'] = int(input('Ano de contratacao: '))
        pessoa['aposentadoria'] = 35 - (date.today().year - pessoa['contratacao']) + pessoa['idade']
        pessoa['salario'] = int(input('Salario: R$'))
        break

for k, v in pessoa.items():
    print(f'{k} tem valor {v}')
