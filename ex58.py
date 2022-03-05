from random import randint

computador = randint(0, 10)
palpites = 0
acertou = False
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
while not acertou:
    jogador = int(input('Digite o número que o computador está pensando: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mai uma vez. ')
print('Acertou! eu estava pensando em {}, você deu {} palpites'.format(computador, palpites))

