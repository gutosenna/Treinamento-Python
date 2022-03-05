n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('>>>>>>> Escolha a opção: '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opcao == 2:
        mult = n1 * n2
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, mult))
    elif opcao == 3:
        if n1 > n2:
            print('O {} é maior que {}'.format(n1, n2))
        else:
            print('O {} é maior que {}'.format(n2, n1))
    elif opcao == 4:
        continue
    elif opcao == 5:
        print('Vc saiu do programa!!!')
        break
