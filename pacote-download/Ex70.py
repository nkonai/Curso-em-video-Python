s = 0
cont = 0
barato = 0
bproduto = ' '
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preco: R$ '))
    choice = ' '
    while choice not in 'SN':
        choice = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if preco >= 1000:
        cont += 1
    if s == 0 or preco < barato:
        barato = preco
        bproduto = produto
    s += preco
    if choice =='N':
        break
print('''
O total da compra foi R${:.2f}
Temos {} produtos custando mais de R$1000
O produto mais barato foi {} que custa R${:.2f}
'''.format(s, cont,bproduto, barato))