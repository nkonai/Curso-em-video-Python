f = str(input('Digite uma frase: '))
f = f.strip().replace(' ','').lower()
s = 0
for c in range(0,len(f)):
    if f[c] == (f[-(1 + c)]):
        s = s + 1
if s == len(f):
    print('E um palindromo')
else:
    print('Nao e um palindromo')
