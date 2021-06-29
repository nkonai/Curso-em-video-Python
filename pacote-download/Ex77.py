palavras = ('aprender','programar','caderno','sol','mar','verao')
print(palavras)
for p in palavras:
    print('\nNa palavra {} temos '.format(p.upper()),end='')
    for l in p:
        if l.lower().strip() in 'aeiou':
            print(l, end=' ')