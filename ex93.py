# Exercício Python 093: Cadastro de Jogador de Futebol
# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida. No final,
# tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante
# o campeonato.

dicionario = dict(nome=str(input('Nome do Jogador: ')).capitalize())
gols = list()
tot = 0
partida = int(input(f'Quantas partidas {dicionario["nome"]} jogou? '))
for ptds in range(partida):
    gols.append(int(input(f'{"":>5}Quantos gols na partida {ptds}? ')))
    tot = sum(gols)
dicionario['gols'] = gols[:]
dicionario['total'] = tot
print('-=' * 30)
print(dicionario)
print('-=' * 30)
for k, v in dicionario.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {dicionario["nome"]} jogou {partida} partidas.')
for i in range(len(gols)):
    print(f'{"":>3}=> Na partida {i}, fez {gols[i]} gols.')
print(f'Foi um total de {tot} gols.')

print(f'O jogador {dicionario["nome"]} jogou {len(dicionario["gols"])} partidas.')
for i, v in enumerate(dicionario['gols']):
    print(f'{"":>3}=> Na partida {i}, fez {v} gols.')
print(f'Foi um total de {dicionario["total"]} gols.')