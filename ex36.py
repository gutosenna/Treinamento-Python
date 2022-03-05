valor = float(input('Qual é o valor da casa? '))
salario = float(input('Qual é o valor do salario do cliente? '))
anos = int(input('Em quantos anos deseja pagar? '))
prestacao = valor / (anos * 12)
minimo =salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(valor, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Emprestimo \033[0:32mCONCEDIDO!\033[m')
else:
    print('Emprestimo \033[0:31mNEGADO!\033[m')