# Exercício Python 090: Dicionário em python
# Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.
pessoa = {}
pessoa['Nome'] = str(input('Nome: ').capitalize())
pessoa['Media'] = float(input(f'Média de {pessoa["Nome"]}: '))

if pessoa['Media'] <= 5:
    pessoa['Situação']= ' está reprovado!'
elif pessoa['Media'] >= 7:
    pessoa['Situação']= ' está aprovado!'
else:
    pessoa['Situação'] = ' está de recuperação!'
for k, v in pessoa.items():
    print(f'{k} é igual a {v}')
