def leiaint(n):
    num = input('Digite um numero: ')
    while num.isnumeric()==False:
        print('\033[0;31mERRO! Digite um numero inteiro valido.\033[m')
        num = input('Digite um numero: ')
    return num

n = leiaint('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}.')