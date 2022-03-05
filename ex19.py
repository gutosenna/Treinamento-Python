from random import choice
n1 = str(input('Digite o Primeiro Aluno: '))
n2 = str(input('Digite o Segundo Aluno: '))
n3 = str(input('Digite o Terceiro Aluno: '))
n4 = str(input('Digite o Quarto Aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print(f'O escolhido foi {escolhido}')
