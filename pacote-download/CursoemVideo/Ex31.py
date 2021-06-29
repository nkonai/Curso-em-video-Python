dist = float(input('Qual a distancia da viagem?'))
if dist<=200:
    print('O valor da passagem e {}'.format(dist*0.5))
else:
    print('O valor da passagem e {}'.format(dist*0.45))