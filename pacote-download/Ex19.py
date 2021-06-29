import random
a1 = input('Primeiro Aluno:')
a2 = input('Segundo aluno:')
a3 = input('Terceiro aluno:')
a4 = input('Quarto aluno:')
lista=[a1,a2,a3,a4]
n=random.choice(lista)
print('O aluno sorteado e {}'.format(n))

