pessoa = []
dado = []
cont = 0
pmax = pmin = 0
maxpessoa = []
minpessoa = []
while True:
    dado.append(str(input('Digite o nome: ')))
    dado.append(float(input('Digite o peso: ')))
    pessoa.append(dado[:])
    cont += 1
    if cont == 1:
        pmax = pmin = dado[1]
    else:
        if cont > 1 and dado[1] > pmax:
            pmax = dado[1]
        if cont > 1 and dado[1] < pmin:
            pmin = dado[1]
    answer = input('Quer continuar? [S/N]: ')
    if answer in "Nn":
        break
    dado.clear()
for i in pessoa:
    print(i)
    if i[1]==pmax:
        maxpessoa.append(i[0])
    else:
        if i[1]==pmin:
            minpessoa.append(i[0])


print(f'Ao todo voce cadastrou {cont} pessoas.')
print(f'O maior peso foi {pmax}kg. Peso de {maxpessoa}')
print(f'O menor peso foi {pmin}kg. Peso de {minpessoa}')