def metade(preco = 0):
    return preco/2

def dobro(preco = 0):
    return preco * 2

def aumentar(preco = 0,r = 0):
    return preco * (100 + r)/100

def diminuir(preco = 0,r = 0):
    return preco * (100 - r)/100

def moeda(preco = 0, moeda = 'R$'):
    return (f'{moeda}{preco:.2f}'.replace('.',','))

