def metade(preco,sit):
    if sit==True:
        return (f'R${preco/2}')
    else:
        return preco/2

def dobro(preco,sit):
    if sit==True:
        return (f'R${preco * 2}')
    else:
        return preco * 2

def aumentar(preco,r,sit):
    if sit==True:
        return (f'R${preco * (100 + r)/100}')
    else:
        return preco * (100 + r) / 100

def diminuir(preco,r,sit):
    if sit==True:
        return(f'R${preco * (100 - r)/100}')
    else:
        return preco * (100-r)/100

def moeda(preco):
    return (f'R${preco}')

def resumo(p,r,q):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'Preco analisado:',end='')
    print(f'{moeda(p):>10}')
    print(f'Dobro do preco:',end='')
    print(f'{dobro(p, True):>10}')
    print(f'Metade do preco:', end='')
    print(f'{metade(p, True):>10}')
    print(f'{r}% de aumento:', end='')
    print(f'{aumentar(p, r, True):>10}')
    print(f'{q}% de reducao:', end='')
    print(f'{diminuir(p, q, True):>10}')