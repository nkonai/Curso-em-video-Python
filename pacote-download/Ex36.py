valor = float(input('Qual o valor do imovel?:'))
salario = float(input('Qual e o seu salario mensal?'))
anos = int(input('Em quantos anos quer quitar o imovel?'))
prestacao = valor/(anos*12)
if salario*0.3<prestacao:
    print('Sinto muito, seu emprestimo foi negado.')
else:
    print('Seu emprestimo foi concedido.')
print('O valor da prestacao mensal nos proximos {} anos e ${:.1f}'.format(anos,prestacao))