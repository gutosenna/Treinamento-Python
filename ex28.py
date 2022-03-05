import random
from time import sleep

jogador = int(input('Qual número estou pensando? '))
print('PROCESSANDO...')
sleep(2)
computador = (random.randint(0,5))
if jogador == computador:
    print('ACERTOU!')
else:
    print('ERROU!')
print(f'O número sorteado foi {computador}')
