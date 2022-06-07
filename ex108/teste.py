# Exercício Python 108: Formatando Moedas em Python
# Adapte o código do desafio #107,
# criando uma função adicional chamada moeda()
# que consiga mostrar os números como um valor monetário formatado.
from ex108 import moeda

n = float(input('Digite o preço: R$ '))
t = float(input('Digite a taxa para avaliação (%): '))
print(f'Aumentando {t:.2f}%, temos {moeda.moeda(moeda.aumentar(n, t))}')
print(f'Diminuindo {t:.2f}%, temos {moeda.moeda(moeda.diminuir(n, t))}')
print(f'O dobro de {moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))}')
print(f'A metade de {moeda.moeda(n)} é {moeda.moeda(moeda.metade(n))}')
