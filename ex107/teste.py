# Exercício Python 107: Exercitando módulos em Python
# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.
import moeda

n = float(input('Digite o preço: R$ '))
moeda.metade(n)
moeda.dobro(n)
moeda.aumentar(n, 10)
moeda.diminuir(n, 10)
