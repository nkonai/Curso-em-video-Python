numero = str(input('Digite um numero de 0 a 9999:'))
unidade = numero[3]
dezena = numero[2]
centena = numero[1]
milhar = numero[0]
print('''unidade:{},
centena:{},
dezena:{},
milhar:{}'''.format(unidade,dezena,centena,milhar))