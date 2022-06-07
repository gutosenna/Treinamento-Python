# Exercício Python 110: Reduzindo ainda mais seu programa
# Adicione o módulo moeda.py criado nos desafios anteriores,
# uma função chamada resumo(),
# que mostre na tela algumas informações geradas pelas funções
# que já temos no módulo criado até aqui.
from ex110 import moeda

n = float(input('Digite o preço: R$ '))
t1 = float(input('Digite a taxa de aumento (%): '))
t2 = float(input('Digite a taxa de redução (%): '))
moeda.resumo(n, t1, t2)
