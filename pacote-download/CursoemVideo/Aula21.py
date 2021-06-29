def fatorial(num = 0):
    f = 1
    for c in range(num,0,-1):
        f *= c
    return f

n = int(input('Digite um numero: '))
print(f'O fatorial de {n} e {fatorial(n)}')