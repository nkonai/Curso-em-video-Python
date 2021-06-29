list = [[],[]]
for v in range(1,8):
    numero = int(input(f"Digite o {v}o. valor: " ))
    if numero%2 == 0:
        list[0].append(numero)
    else:
        list[1].append(numero)
print(f'Os valores pares digitados foram: {sorted(list[0])}')
print(f'Os valores impares digitados foram: {sorted(list[1])}')

