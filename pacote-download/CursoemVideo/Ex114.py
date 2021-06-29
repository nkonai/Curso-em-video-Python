import urllib
import urllib.request
try:
    pagina = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim nao esta acessivel no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso!')
    print(pagina.read())