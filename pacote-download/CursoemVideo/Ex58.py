import random
pc = random.randint(0,10)
print('Sou seu computador...Acabei de pensar em um numero de 0 a 10.')
print('Consegue adivinhar qual foi?')
count = 0
acertou = False
while not acertou:
    guess = int(input('Qual e seu palpite?  '))
    count = count + 1
    if guess == pc:
        acertou = True
    else:
        if guess < pc:
            print('Mais...tente mais uma vez!')
        elif guess > pc:
            print('Menos...Tente mais uma vez.')

print('Acertou! Voce teve {} palpites e o numero era {}'.format(count,pc))


