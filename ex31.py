distancia = int(input('Qual a distância percorrida? '))
if distancia <= 200:
    preço = distancia* 0.50
    print('O valor da viagem foi {:.2f}'.format(preço))
else:
    preço = distancia * 0.45
    print('O valor da viagem foi {:.2f}'.format(preço))