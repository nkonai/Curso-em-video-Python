from datetime import date
ano = int(input('Qual e o ano de seu nascimento?'))
anoatual = date.today().year
diff = anoatual - ano
alistamento=18
if diff<18:
    print('Falta {} anos para seu alistamento'.format(alistamento-diff))
elif diff==18:
    print('E hora de se alistar')
else:
    print('Ja passaram {} anos desde o ano de seu alistamento'.format(diff-alistamento))