n = int(input('Digite um numero: '))
count = 0
for c in range(1,n+1):
    if n%c==0:
        count = count + 1
if count == 2:
    print('Este numero e primo')
else:
    print('Este numero nao e primo')
