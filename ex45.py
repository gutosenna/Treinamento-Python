import random
from time import sleep

opcao = int(input('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Qual é a sua jogada? '''))
computador = random.randint(0, 2)
escolha = ('PEDRA', 'PAPEL', 'TESOURA')
print('JO', end='')
sleep(1)
print('KEN', end='')
sleep(1)
print('PO!!!')
sleep(1)
print('JOGADOR {} X COMPUTADOR {}'.format(escolha[opcao], escolha[computador]))
if opcao == computador:
    print('\033[33mEMPATE!\033[m')
elif opcao == 0 and computador == 1:
    print('\033[31mPERDEU!\033[m')
elif opcao == 0 and computador == 2:
    print('\033[32mGANHOU!\033[m')
elif opcao == 1 and computador == 2:
    print('\033[31mPERDEU!\033[m')
elif opcao == 1 and computador == 0:
    print('\033[32mGANHOU!\033[m')
elif opcao == 2 and computador == 1:
    print('\033[32mGANHOU!\033[m')
elif opcao == 2 and computador == 0:
    print('\033[31mPERDEU!\033[m')
