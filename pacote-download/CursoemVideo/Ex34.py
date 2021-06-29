salario = float(input('Qual e o seu salario?'))
if salario<=1250:
    print('Seu salario com aumento de 15% sera {}'.format(salario*1.15))
else:
    print('Seu salario com aumento de 10% sera {}'.format(salario*1.1))
