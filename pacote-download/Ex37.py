num = int(input('Digite um numero inteiro:'))
print('''Escolha uma das bases para conversao:'
[1] converter para BINARIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opcao = int(input('Sua opcao:'))
if opcao == 1:
    print('{} convertido para binario e igual a {}'.format(num,bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para octal e igual a {}'.format(num,oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para hexadecimal e igual a {}'.format(num,hex(num)[2:]))
else:
    print('opcao invalida')

