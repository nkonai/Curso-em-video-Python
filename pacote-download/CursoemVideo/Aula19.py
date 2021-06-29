pessoas = {'nome' : 'Gustavo','sexo' : 'M','idade' : 22}
print(pessoas.items())

for k in pessoas.keys():
    print(k)

for v in pessoas.values():
    print(v)

for k,v in pessoas.items():
    print(f'{k} = {v}')

del pessoas['sexo']
print(pessoas)

pessoas['nome'] = 'Leandro'
print(pessoas)
pessoas['peso'] = 98.5
print(pessoas)

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for k,v in e.items():
        print(f'O campo {k} tem valor {v}.')