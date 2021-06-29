list = [[0,0,0],[0,0,0],[0,0,0]]
spar = mai = scol = 0
for a in range(0,3):
    for b in range(0,3):
        list[a][b] = int(input(f'Digite um valor para [{a},{b}]: '))

for a in range(0,3):
    for b in range(0,3):
        print(f'[{list[a][b]:^5}]', end='')
        if list[a][b]%2 == 0:
            spar += list[a][b]
    print()

for a in range(0,3):
    scol += list[a][2]

for b in range(0,3):
    if b == 0:
        mai = list[1][b]
    elif list [1][b] > mai:
        mai = list[1][b]

print(f'A soma dos valores pares e {spar}.')
print(f'A soma dos valores da terceira coluna e {scol}.')
print(f'O maior valor da segunda linha e {mai}')