def metade(preco,sit):
    if sit:
        return (f'R${preco/2}')
    else:
        return preco/2

def dobro(preco,sit):
    if sit:
        return (f'R${preco * 2}')
    else:
        return preco * 2

def aumentar(preco,r,sit):
    if sit:
        return (f'R${preco * (100 + r)/100}')
    else:
        return preco * (100 + r) / 100

def diminuir(preco,r,sit):
    if sit:
        return(f'R${preco * (100 - r)/100}')
    else:
        return preco * (100-r)/100

def moeda(preco):
    return (f'R${preco}')

def resumo(p=0, r=10, q=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preco analisado: \t{moeda(p):>10}')
    print(f'Dobro do preco: \t{dobro(p, True):>10}')
    print(f'Metade do preco: \t{metade(p, True):>10}')
    print(f'{r}% de aumento: \t{aumentar(p, r, True):>10}')
    print(f'{q}% de reducao: \t{diminuir(p, q, True):>10}')