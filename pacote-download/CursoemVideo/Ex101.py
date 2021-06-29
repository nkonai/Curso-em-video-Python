def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade >= 18 and idade <= 65:
        print(f'Com {idade} anos: Voto obrigatorio')
    elif idade < 18:
        print(f'Com {idade} anos: Nao vota')
    else:
        print(f'Com {idade} anos: Voto opcional')

nasc = int(input('Em que ano voce nasceu? '))
voto(nasc)