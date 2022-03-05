# print('=' * 10, '=' * 10, 'LOJAS SENNA')
print('{:=^40}'.format(' LOJAS SENNA '))
preço = float(input('Preço das compras: R$'))
print('''
FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro / cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    resultado = preço - (preço * 10 / 100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, resultado))
elif opção == 2:
    resultado = preço - (preço * 5 / 100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, resultado))
elif opção == 3:
    print('Sua compra de R${:.2f} vai custar R${:.2f} SEM JUROS e SEM DESCONTOS.'.format(preço, preço))
elif opção == 4:
    parcelas = int(input('Quantas parcelas? '))
    resultado = preço + (preço * 20 / 100)
    print('''Sua compra será parcelada em {}x de R${:.2f} COM JUROS
Sua compra de R${:.2f} vai custar R${:.2f} no final.'''.format(parcelas, (resultado / parcelas), preço, resultado))
else:
    print('Opção inválida!')
