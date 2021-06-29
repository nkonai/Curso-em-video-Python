import math
a = float(input('Digite o comprimento de uma reta:'))
b = float(input('Digite o comprimento de outra reta:'))
c = float(input('Digite o comprimento de uma terceira reta:'))

if abs(b-c)<a and a<(b+c) and abs(a-c)< b and b<(a+c) and abs(a-b)<c and c<(a+b):
    print('Formam um triangulo')
else:
    print('Nao formam um triangulo')
