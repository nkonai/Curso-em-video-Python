from datetime import date
hoje = date.today().year
s = 0
a = 7
for c in range(1,a+1):
    n = int(input('Ano de nascimento {}: '.format(c)))
    if hoje - n >= 21:
        s = s + 1
print('{} pessoa(s) maior de idade e {} ainda nao'.format(s,a-s))