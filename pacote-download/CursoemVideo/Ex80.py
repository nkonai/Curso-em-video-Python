list = []

for c in range(0,5):
    numero = int(input('Digite um valor: '))
    if c ==0 or numero > list[-1]:
        list.append(numero)
        print('Adicionado ao final da lista')

    else:
        pos = 0
        while pos < len(list):
            if numero <= list[pos]:
                list.insert(pos,numero)
                print(f'Adicionado na posicao {pos} da lista')
                break
            pos += 1
print(f'Os valores digitados foram {list}')
