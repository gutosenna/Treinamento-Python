# Exercício Python 20: Sorteando uma ordem na lista
# O mesmo professor do desafio 19 quer sortear a ordem de
# apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e
# mostre a ordem sorteada.

import random
nome = [input('Primeiro: '), input('Segundo: '), input('Terceiro: '), input('Quarto? ')]
random.shuffle(nome)
print(f'Primeiro = {nome[0]}, Segundo = {nome[1]}, Terceiro = {nome[2]} e Quarto = {nome[3]}')
