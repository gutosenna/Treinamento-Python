# Exercício Python 111: Transformando módulos em pacotes
# Crie um pacote chamado utilidadesCeV
# que tenha dois módulos internos chamados moeda e dado.
# Transfira todas as funções utilizadas nos desafios
# 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.
from ex112.utilidades import moeda
from ex112.utilidades import dado

n = dado.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(n, 5, 2)


