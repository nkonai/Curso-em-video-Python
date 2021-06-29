
def maior(lst):
    print('-=' * 20)
    print('Analisando os valores passados...')
    ma = 0
    count = 0
    for n in lst:
        print(n, end=' ')
        if count == 0:
            ma = n
        else:
            if n > ma:
                ma = n
        count += 1
    print(f'Foram informados {count} valores')
    print(f'O maior valor informado foi {ma}')
    print('-=' * 20)

valores = [2,9,4,5,7,1]
maior(valores)

valores = [4,7,0]
maior(valores)