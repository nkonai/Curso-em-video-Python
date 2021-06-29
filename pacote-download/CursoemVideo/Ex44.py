preco = float(input('Valor do produto:R$'))
pgm = int(input('''Selecione a forma de pagamento 1,2, 3 ou 4:
 [1] a vista em dinheiro ou cheque;
 [2] a vista no cartao;
 [3] em ate 2X no cartao;
 [4] 3X ou mais no cartao
 Qual e a opcao?'''))
if pgm == 1:
    print('Sua compra de R${} vai custar R${:.2f}'.format(preco,preco*0.9))
elif pgm == 2:
    print('Sua compra de R${} vai custar R${:.2f}'.format(preco,preco*0.95))
elif pgm == 3:
    print('Sua compra vai custar R${:.2f} em 2 parcelas de R${:.2f}'.format(preco,preco/2))
elif pgm == 4:
    parcelas = int(input('Numero de parcelas:'))
    print('Sua compra vai custar R${:.2f} sera parcelada em {}x de R${:.2f} COM JUROS'.format(preco*1.2,parcelas,(preco*1.2)/parcelas))
else:
    print('Opcao de pagamento invalida')