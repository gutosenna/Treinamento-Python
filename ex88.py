#Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.
from random import randint as rd
from time import sleep

lista, sena = list(), list()
print('-' * 30)
print('     JOGA NA MEGA SENA     ')
print('-' * 30)
resp = int(input('Quantos jogos quer que eu sorteie? '))
tot = 0
while tot < resp:
    cont = 0
    while True:
        num = rd(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    sena.append(lista[:])
    lista.clear()
    tot += 1
for c in range(len(sena)):
    sleep(0.8)
    print(f'Jogo {c+1}: {sena[c]}')
