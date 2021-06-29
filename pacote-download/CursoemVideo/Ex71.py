c50 = c20 = c10 = c1 = 0
s = 0
n = int(input('Que valor voce quer sacar? R$'))
total = n
ced = 50
totced = 0
while True:
    if total >= ced:
        totced +=1
        total -=ced
    else:
        print('Total de {} cedulas de R${}.'.format(totced,ced))
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('='*30)
print('Volte sempre ao Banco!')