# Exercício Python 109: Formatando Moedas em Python 2
# Modifique as funções que foram criadas no desafio 107
# para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado
# pela função moeda(), desenvolvida no desafio 108.
from ex109 import moeda

n = float(input('Digite o preço: R$ '))
t = float(input('Digite a taxa para avaliação (%): '))
print(f'Aumentando {t}%, temos {moeda.aumentar(n, t, True)}')
print(f'Diminuindo {t}%, temos {moeda.diminuir(n, t, True)}')
print(f'O dobro de {moeda.moeda(n)} é {moeda.dobro(n, True)}')
print(f'A metade de {moeda.moeda(n)} é {moeda.metade(n, True)}')
