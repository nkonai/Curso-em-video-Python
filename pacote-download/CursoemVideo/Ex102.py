
def fatorial(num, show=False):
    """
    Calcula o fatorial de um numero
    :param num: O numero a ser calculado
    :param show: (opcional) Mostrar ou nao a conta
    :return: O valor fatorial do numero n
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end ='')
            else:
                print(' = ', end ='')
        f *= c
    return f

print(fatorial(5, show=True))
help(fatorial)