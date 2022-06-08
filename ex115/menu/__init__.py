def menu():
    print('-' * 35)
    print('MENU PRINCIPAL'.center(35))
    print('-' * 35)
    print('\033[33m1\033[m - \033[34mVer pessoas cadastradas\033[m')
    print('\033[33m2\033[m - \033[34mCadastrar nova Pessoa\033[m')
    print('\033[33m3\033[m - \033[34mSair do Sistema\033[m')
    print('-' * 35)


def opcao():
    n = int(input('Sua Opção: '))
    op = (1, 2, 3)
    if n == op[0]:
        print('-' * 35)
        print(f'Opção {op[0]}')
        print('-' * 35)
    elif n == op[1]:
        print('-' * 35)
        print(f'Opção {op[1]}')
        print('-' * 35)
    elif n == op[2]:
        print('-' * 35)
        print(f'Saindo do sistema... Até logo!')
        print('-' * 35)
