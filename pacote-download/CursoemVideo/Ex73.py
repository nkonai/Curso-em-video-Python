brasileirao = ('Palmeiras','Flamengo','Internacional',
               'Gremio','Sao Paulo','Atletico MG',
               'Athletico PR','Cruzeiro','Botafogo',
               'Santos','Bahia','Fluminense','Corinthians',
               'Chapecoense','Ceara','Vasco','Sport',
               'America MG','Vitoria','Parana')
print(f'Os 5 primeiros sao: {brasileirao[:5]}')
print(f'Os 4 ultimos sao: {brasileirao[-4:]}')
print(f'Times em ordem alfabetica: {sorted(brasileirao)}')
print(f'''O Chapecoense esta na {brasileirao.index('Chapecoense')+1}a posicao''')
