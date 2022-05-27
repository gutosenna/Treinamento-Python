# Jogo de dados em python - Melhorado
import random
from operator import itemgetter
from time import sleep

def dados1():
    print("+------------+")
    print("|            |")
    print("|      0     |")
    print("|            |")
    print("+------------+")

jogada, ranking = dict(), list()
print('Valores sorteados:')
for k in range(1, 5):
    jogada[f'Jogador {k}'] = random.randint(1, 6)
for k, v in jogada.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('-=' * 30)
print(' == RANKING DOS JOGADORES == ')
ranking = sorted(jogada.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}° Lugar {v[0]} com {v[1]}')
    sleep(1)
dados1()