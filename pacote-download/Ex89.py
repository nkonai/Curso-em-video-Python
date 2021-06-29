list = []
pessoa = []
dado =[]
media = 0
cont = 0
while True:
    nome = str(input('Nome: '))
    pessoa.append(nome)
    nota1 = float(input('Nota 1: '))
    dado.append(nota1)
    nota2 = float(input('Nota 2: '))
    dado.append(nota2)
    media = (nota1+nota2)/2
    dado.append(media)
    pessoa.append(dado[:])
    list.append(pessoa[:])
    cont += 1
    pessoa.clear()
    dado.clear()
    answer = input('Quer continuar? [S/N]: ')
    if answer in 'Nn':
        break

print('-='*30)
for p in range(0,cont):
    print(f'{p:<4} {list[p][0]:<10}   {list[p][1][2]:>8}')

while True:
    escolha = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if escolha ==999:
        break
    elif escolha in range(0,cont):
        print(f'As notas de {list[escolha][0]} sao {list[escolha][1][0]} e {list[escolha][1][1]}')



