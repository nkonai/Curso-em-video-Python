def metade(preco,sit):
    if sit==True:
        return (f'R${preco/2:.2f}'.replace('.',','))
    else:
        return preco/2

def dobro(preco,sit):
    if sit==True:
        return (f'R${preco * 2:.2f}'.replace('.',','))
    else:
        return preco * 2

def aumentar(preco,r,sit):
    if sit==True:
        return (f'R${preco * (100 + r)/100:.2f}'.replace('.',','))
    else:
        return preco * (100 + r) / 100

def diminuir(preco,r,sit):
    if sit==True:
        return(f'R${preco * (100 - r)/100:.2f}'.replace('.',','))
    else:
        return preco * (100-r)/100

def moeda(preco):
    return (f'R${preco:.2f}'.replace('.',','))
