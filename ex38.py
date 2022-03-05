n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
if n1 > n2:
    print('O numero {} eh maior que {}'.format(n1, n2))
elif n2 > n1:
    print(f'O numero {n2} eh maior que {n1}')
else:
    print('Os numeros são iguais!')