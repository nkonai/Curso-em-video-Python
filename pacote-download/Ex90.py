pessoa = dict()

pessoa['nome'] = str(input('Nome: '))
pessoa['media'] = float(input(f'Media de {pessoa["nome"]}: ' ))

if pessoa['media'] < 5:
    pessoa['situacao'] = 'reprovado'
else:
    pessoa['situacao'] = 'aprovado'

for k, v in pessoa.items():
    print(f'{k} e igual a {v}')
