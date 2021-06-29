list=[]
expressao = input('Digite sua expressao: ')
for s in expressao:
    if s =='(':
        list.append('(')
    elif s == ')':
        if len(list)>0:
            list.pop()
        else:
            list.append(')')
            break
if len(list)==0:
    print('Sua expressao esta valida!')
else:
    print('Sua expressao esta errada!')