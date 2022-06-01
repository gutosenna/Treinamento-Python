# Exercício Python 103: Ficha do Jogador
# Faça um programa que tenha uma função chamada ficha(),
# que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.
def ficha(jogador='<desconhecido>', gol=0):
    """
    -> Função que mostra a ficha do jogador
    :param jogador: String
    :param gol: int
    :return: sem retorno
    """
    print(f'O jogador {jogador} fez {gol} gol(s) no campeonato.')


print('-' * 20)
nome = str(input('Nome do Jogador: '))
gols = str(input("Número de Gols: "))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gol=gols)
else:
    ficha(nome, gols)
# help(ficha)
