#Quando declaramos uma lista Python com num = [3, 6, 4, 1] e executamos a estrutura for n1, n2 in enumerate(num): com o comando print(n1 + n2) dentro do bloco do laço, quais valores serão exibidos?
num = [3,6,4,1]
for count, value in enumerate(num):
    print(count, value)