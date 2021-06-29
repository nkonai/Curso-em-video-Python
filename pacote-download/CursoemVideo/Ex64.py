n = 0
s = 0
c = 0
n = int(input('Digite um numero:'))
while n !=999:
    s = s + n
    c = c + 1
    n = int(input('Digite um numero:'))
print('{} foram digitados e a soma dos numeros e {}'.format(c,s))