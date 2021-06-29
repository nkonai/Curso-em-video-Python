nomevelho = 0
idade = 0
idadeh = 0
m = 0
a = 4
for c in range(1,a+1):
    n = str(input('Digite o nome {}: '.format(c)))
    i = int(input('Digite a idade {}: '.format(c)))
    s = str(input('Digite o sexo [F] [M] {}: '.format(c)))
    idade = idade + i
    if s =='M' and i>idadeh:
        nomevelho=n
        idadeh = i
    if s =='F' and i<20:
        m = m+1

media = idade/a
print('A media de idade do grupo e {}'.format(media))
print('O nome do homem mais velho e {} e ele tem {} anos'.format(nomevelho,idadeh))
print('{} mulheres tem menos de 20 anos'.format(m))