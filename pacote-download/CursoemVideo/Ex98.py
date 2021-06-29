from time import sleep
def contagem(inicio,fim,meio):
    print('-='*20)
    print(f'Contagem de {inicio} ate {fim} de {meio} em {meio}')
    sleep(2)
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(cont,end=' ')
            sleep(0.3)
            cont += meio
    else:
        cont = inicio
        while cont > fim:
            print(cont, end=' ')
            sleep(0.3)
            cont -= meio
    print('FIM!')


contagem(1,10,1)
contagem(0,100,10)
contagem(10,1,2)

print('Agora e a sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fi = int(input('Fim: '))
passo = int(input('Passo: '))
contagem(ini,fi,passo)