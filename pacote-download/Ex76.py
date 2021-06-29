lista = ('Lapis',1.75,'Borracha',2,'Caderno',15.9,'Estojo',25,'Transferidor',4.2,'Compasso',9.99,'Mochila',120.32,'Canetas',22.3,'Livro',34.90)
print(lista)

print('-'*40)
print('{:^40}'.format('LISTAGEM DE PRECO'))
print('-'*40)

for n in range(len(lista)):
    if n%2==0:
        print(f'{lista[n]:.<30}',end='')
    else:
        print(f'R${lista[n]:>7.2f}')
print('-'*40)


