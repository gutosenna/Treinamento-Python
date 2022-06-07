# Exercício Python 113: Funções aprofundadas em Python
# Reescreva a função leiaInt() que fizemos no desafio 104,
# incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
from utilidades import dados

inteiro = dados.leiaInt('Digite um inteiro: ')
real = dados.leiaFloat('Digite um número Real: ')
print(f'O número inteiro foi {inteiro} e o número real foi {real}.')