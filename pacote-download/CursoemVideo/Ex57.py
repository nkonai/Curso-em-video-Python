p = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
while p not in 'MF':
    print('Opcao nao valida.')
    p = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(p))

