def metade(preco):
    return preco/2

def dobro(preco):
    return preco * 2

def aumentar(preco,r):
    return preco * (100 + r)/100

def diminuir(preco,r):
    return preco * (100 - r)/100

def moeda(preco):
    return (f'R${preco}')