n = int(input('Digite um numero: '))
s = n
f = 1
print('Calculando {}! = '.format(n))
while s > 0:
    print('{} '.format(s), end='')
    print(' x ' if s > 1 else ' = ', end='')
    f = f * s
    s = s - 1
print(' {}'.format(f))