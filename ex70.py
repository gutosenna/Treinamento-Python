produtosMil = total = cont = menor = maior = 0
barato = ''
print('-'*30)
print('\tLOJA SUPER BARATÃO')
print('-'*30)
while True:
    nome = str(input('Nome do Produto: ')).strip()
    preço = float(input('Preço: R$'))
    opcao = str(input('Quer continuar? [S/N] ')).strip()
    total += preço
    cont += 1
    if cont == 1:
        maior = menor = preço
    else:
        if preço > maior:
            maior = preço
        if preço < menor:
            menor = preço
            barato = nome
    if preço > 1000:
        produtosMil += 1
    elif opcao in 'Nn':
        break
print('FIM DO PROGRAMA')
print('O total da compra foi R${:.2f}'.format(total))
print('Temos {} produtos custando mais de R$1000,00'.format(produtosMil))
print('O produto mais barato foi {} que custa R${}'.format(barato, menor))





