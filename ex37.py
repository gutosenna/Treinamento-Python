numero = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
        [ 1 ] converter para BINÁRIO
        [ 2 ] converter para OCTAL
        [ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    convertido = bin(numero)
    print('{} convertido para BINÁRIO é igual a {}'.format(numero, convertido[2:]))
elif opcao == 2:
    convertido = oct(numero)
    print('{} convertido para OCTAL é igual a {}'.format(numero, convertido[2:]))
elif opcao == 3:
    convertido = hex(numero)
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero, convertido[2:]))
else:
    print('Opção inválida')
