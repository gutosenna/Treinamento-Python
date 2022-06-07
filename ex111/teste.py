# Exercício Python 111: Transformando módulos em pacotes
# Crie um pacote chamado utilidadesCeV
# que tenha dois módulos internos chamados moeda e dado.
# Transfira todas as funções utilizadas nos desafios
# 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.
from ex111.utilidades import moeda

n = float(input('Digite o preço: R$ '))
t1 = float(input('Digite a taxa de aumento (%): '))
t2 = float(input('Digite a taxa de redução (%): '))
moeda.resumo(n, t1, t2)
