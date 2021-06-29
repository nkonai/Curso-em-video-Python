n1 = float(input('Digite sua primeira nota:'))
n2 = float(input('Digite sua segunda nota:'))
media = (n1 + n2)/2
if media<5:
    print('REPROVADO, sua media foi {:.1f}'.format(media))
elif media>=5 and media<=6.9:
    print('RECUPERACAO, sua media foi {:.1f}'.format(media))
else:
    print('APROVADO, sua media foi {:.1f}'.format(media))