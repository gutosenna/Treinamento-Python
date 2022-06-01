# Exercício Python 100: Funções para sortear e somar
# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e
# a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
import random
from time import sleep

números = []

def sorteia():
    """
    -> sorteia uma lista de 5 valores aleatórios
    :return: sem retorno
    """
    print(f'Sorteando 5 valores da lista: ', end='')
    for c in range(5):
        num_sorteado = random.randint(0, 10)
        números.append(num_sorteado)
    for c in números:
        sleep(0.5)
        print(c, end=' ')
    sleep(0.5)
    print('PRONTO!')
    somaPar(números)

def somaPar(*lista):
    """
    -> Soma somente números pares da lista
    :param lista: lista de valores
    :return: sem retorno
    """
    soma = 0
    for v in lista:
        for i in v:
            if i % 2 == 0:
                soma += i
    print(f'Somando os valores pares de {lista[0]}, temos {soma}')


sorteia()

