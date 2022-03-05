velocidade = int(input('Qual é a velocidade do carro? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Vc teve uma multa de R${:.2f}'.format(multa))
else:
    print('Vc está na velocidade da via!')