from time import sleep
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
s = 0
while s!=5:
    print('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair do programa
        ''')
    s = int(input('>>>>>>Qual e a sua opcao? '))
    if s == 1:
        print('A soma e {}'.format(n1 + n2))
    elif s == 2:
        print('A multiplicacao e {}'.format(n1*n2))
    elif s == 3:
        print('O maior numero e {}'.format(max(n1,n2)))
    elif s == 4:
        print('Informe os numeros novamente')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif s == 5:
        print('Finalizando...')
    else:
        print('Opcao invalida!')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')