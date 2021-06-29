min = 0
max = 0
for c in range(1,6):
    p = float(input('Digite o peso {}: '.format(c)))
    if c ==1:
        min = p
        max = p
    else:
        if p > max:
            max = p
        if p < min:
            min = p
print('O maior peso foi {}kg e o menor peso foi {}kg'.format(max,min))
