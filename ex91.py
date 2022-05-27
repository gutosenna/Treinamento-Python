# Exercício Python 091: Jogo de dados em python
# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
import random
from operator import itemgetter
from time import sleep

jogada, ranking = dict(), list()
print('Valores sorteados:')
for k in range(1, 5):
    jogada[f'Jogador {k}'] = random.randint(1, 6)
for k, v in jogada.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('-=' * 30)
print(' == RANKING DOS JOGADORES == ')
# for i in sorted(jogada, key=jogada.get, reverse=True):
#     lugar = jogada.copy()
ranking = sorted(jogada.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}° Lugar {v[0]} com {v[1]}')
    sleep(1)
