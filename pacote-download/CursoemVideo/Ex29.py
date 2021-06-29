velocidade = float(input('Velocidade do carro em km:'))
if velocidade >80:
    print('Voce foi multado no valor de {:.2f} reais'.format((velocidade-80)*7))
print('end')