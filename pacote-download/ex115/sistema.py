from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        print(linha())
        print('OPCAO 1'.center(30))
        print(linha())
        #Opcao de listar o conteudo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        print(linha())
        print('OPCAO 2'.center(30))
        print(linha())
        #Opcao de cadastrar uma nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)

    elif resposta == 3:
        print(linha())
        print('OPCAO 3'.center(30))
        print(linha())
        print('Saindo do sistema...Ate logo!')
        break
    else:
        print('\033[31mErro! Digite uma opcao valida!\033[m')
    sleep(2)
