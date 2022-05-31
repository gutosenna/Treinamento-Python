# Exercício Python 095: Aprimorando Dicionários
# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

gols, times = list(), list()
dicionario = dict()

while True:
    gols.clear()
    dicionario['nome'] = str(input('Nome do Jogador: ').capitalize())
    partida = int(input(f'Quantas partidas {dicionario["nome"]} jogou? '))
    for ptds in range(partida):
        gols.append(int(input(f'{"":>5}Quantos gols na partida {ptds+1}? ')))
    dicionario['gols'] = gols[:]
    dicionario['total'] = sum(gols)
    times.append(dicionario.copy())
    while True:
        resp = str(input('Quer Continuar? [S/N] '))
        if resp in 'NnSs':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp in 'Nn':
        break
print('-=' * 30)
print(times)
print('-' * 50)
print(f'cod. nome{"gols":>15} {"total":>15}')
print('-' * 50)
for i, v in enumerate(times):
    print(f'{i} {str(v["nome"]):<15} {str(v["gols"]):<15} {str(v["total"]):>15}')
print('-' * 30)
while True:
    dados = int(input('Mostrar dados de qual jogador? (999 para encerrar): '))
    if dados == 999:
        break
    elif dados >= len(times):
        print(f'ERRO! Não existe jogador com código {dados}')
    elif dados < len(times):
        print(f'-- LEVANTAMENTO DO JOGADOR {times[dados]["nome"]}')
        for i, v in enumerate(times[dados]["gols"]):
            print(f'{"":>3}=> No jogo {i+1}, fez {v} gols.')
print('VOLTE SEMPRE!')
