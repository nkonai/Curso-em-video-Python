lista = ('zero','um','dois','tres','quatro',
         'cinco','seis','sete','oito','nove',
         'dez','onze','doze','treze','catorze',
         'quinze','dezesseis','dezessete','dezoito',
         'dezenove','vinte')


opcao = ' '
while opcao not in 'N':
    n = int(input('Digite um numero entre 0 e 20: '))
    while n not in range(0,21):
        n = int(input('Tente novamente. Digite um numero entre 0 e 20: '))
    print(f'Voce digitou o numero {lista[n]}.')
    opcao = str(input('Quer continuar? [S/N]: ')).upper().strip()


