opcao = 'Ss'
cont = soma = maior = menor = 0
while opcao in 'Ss':
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    opcao = str(input('Quer continuar? [S/N] '))
media = soma / cont
print('Você digitou {} números e a média foi {}\n'
      'O maior valor foi {} e o menor foi {}'.format(cont, media, maior, menor))
