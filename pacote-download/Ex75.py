n = 0
cont = 0
par = 0
numeros = (int(input('Digite um numero: ')),
           int(input('Digite um numero: ')),
           int(input('Digite um numero: ')),
           int(input('Digite um numero: ')))

print(numeros)
print('O numero 9 aparece {} vezes'.format(numeros.count(9)))
if 3 in numeros:
    print('O numero 3 apareceu na posicao {}.'.format(numeros.index(3)+1))
else:
    print('O valor 3 nao foi digitado')
print('Os valores pares digitados foram', end=' ')
for n in numeros:
    if n%2==0:
        print(n, end=' ')
