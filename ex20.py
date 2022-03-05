import random
nome = [input('Primeiro: '), input('Segundo: '), input('Terceiro: '), input('Quarto? ')]
random.shuffle(nome)
print(f'Primeiro = {nome[0]}, Segundo = {nome[1]}, Terceiro = {nome[2]} e Quarto = {nome[3]}')
