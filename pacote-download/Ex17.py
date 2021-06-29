import math
l1=float(input('Digite o comprimento do cateto oposto:'))
l2=float(input('Digite o comprimento do cateto adjacente:'))
l3=math.hypot(l1,l2)
print('A hipotenusa de um triangulo retangulo de catetos {:.2f} e {:.2f} e {:.2f}'.format(l1,l2,l3))