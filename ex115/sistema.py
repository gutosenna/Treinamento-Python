from ex115.lib.interface import *
from time import sleep
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        cabecalho('Opção 1')
    elif resposta == 2:
        cabecalho('Opção 2')
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo', cor='red')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)