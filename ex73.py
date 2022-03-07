def tela():
    print('-=' * 50)


times = ('Atletico-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Tarantino',
         'Fluminense', 'America-MG', 'Atletico-GO', 'Santos', 'Ceara SC', 'Internacional',
         'Sao Paulo', 'Athletico-PR', 'Cuiaba', 'Juventude', 'Gremio', 'Bahia', 'Sport', 'Recife',
         'Chapecoense')
tela()
print(f'Lista de times do Brasileirão: {times}')
tela()
print(f'Os 5 primeiros são {times[:5]}')
tela()
print(f'Os últimos 4 são {times[-4:]}')
tela()
print(f'Times em ordem alfabética {sorted(times)}')
tela()
# var = [(n, times[n]) for n, x in enumerate(times) if x == 'Chapecoense']
print(f'O Chapecoense está na {times.index("Chapecoense")+ 1}ª posição.')
