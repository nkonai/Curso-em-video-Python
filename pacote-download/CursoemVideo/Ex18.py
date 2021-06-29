import math
n1 = float(input('Digite um angulo:'))
seno = math.sin(math.radians(n1))
cos = math.cos(math.radians(n1))
tan = math.tan(math.radians(n1))
print('O angulo {:.2f} tem seno {:.2f}, cosseno {:.2f} e tangente {:.2f}'.format(n1,seno,cos,tan))