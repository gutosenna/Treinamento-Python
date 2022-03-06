import random
from time import sleep


def tela(j, c, r, p_i):
    print('-' * 30)
    print(f'Você jogou {j} e o computador {c}. Total de {r} Deu {p_i}')
    print('-' * 30)
    print('Você VENCEU!!!\nVamos jogar novamente...')
    print('=-' * 15)
    sleep(2)


print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)
pontos = 0
while True:
    computador = random.randint(0, 10)
    jogador = int(input('Digite um valor: '))
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    resp = computador + jogador
    if escolha in 'Pp' and resp % 2 == 0:
        pontos += 1
        par_impar = 'PAR'
        tela(jogador, computador, resp, par_impar)
    elif escolha in 'Ii' and resp % 2 != 0:
        pontos += 1
        par_impar = 'IMPAR'
        tela(jogador, computador, resp, par_impar)
    elif escolha not in 'PpIi':
        print('Opção inválida!')
    print('-' * 30)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {resp} ', end='')
    print('DEU PAR' if resp % 2 == 0 else 'DEU ÍMPAR')
    print('-' * 30)
    print('Você PERDEU!!!')
    print('=-' * 15)
    break
print('GAME OVER! Você venceu {} vez(es).'.format(pontos))