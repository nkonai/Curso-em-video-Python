from datetime import date
ano = int(input('Digite o ano de seu nascimento:'))
anoatual = date.today().year
idade = anoatual - ano
if idade <= 9:
    print('MIRIM, o atleta tem {} anos'.format(idade))
elif idade <=14:
    print('INFANTIL, o atleta tem {} anos'.format(idade))
elif idade <=19:
    print('JUNIOR, o atleta tem {} anos'.format(idade))
elif idade <=25:
    print('SENIOR,, o atleta tem {} anos'.format(idade))
else:
    print('MASTER,o atleta tem {} anos'.format(idade))

