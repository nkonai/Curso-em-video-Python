list = []
max = min = 0
for v in range(0,5):
    numero = int(input(f'Digite um valor para a posicao {v}: '))
    list.append(numero)
    if v ==0:
        max = min = numero
    else:
        if numero > max:
            max = numero
        if numero < min:
            min = numero
print(f'Voce digitou os valores {list}')
print(f'O maior valor digitado foi {max} na posicao ',end='')
for i, v in enumerate(list):
    if v == max:
        print(f'{i}...',end='')
print()
print(f'O menor vaor digitado foi {min} na posicao ',end='')
for i, v in enumerate(list):
    if v == min:
        print(f'{i}...',end='')