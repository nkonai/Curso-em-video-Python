list = [[0,0,0],[0,0,0],[0,0,0]]
for a in range(0,3):
    for b in range(0,3):
        list[a][b] = int(input(f'Digite um valor para [{a},{b}]: '))

for a in range(0,3):
    for b in range(0,3):
        print(f'[{list[a][b]:^5}]', end='')
    print()