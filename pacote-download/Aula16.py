lanche = ('hamburger', 'suco', 'pizza', 'pudim')
#Tuplas sao imutaveis
print(len(lanche))
for cont in range(0,len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')


#for comida in lanche:
#    print(f'Eu vou comer {comida}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posicao {pos}')

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(len(c))
print(c.count(5))
print(c.index(2))