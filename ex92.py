# Exercício Python 092: Cadastro de trabalhador em python
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
import datetime as dt

pessoa = dict()

pessoa['Nome'] = str(input('Nome: ')).capitalize()
pessoa['AnoNascimento'] = int(input('Ano de Nascimento: '))
ano = dt.date.today()
anoAtual = ano.year
pessoa['Idade'] = anoAtual - pessoa['AnoNascimento']
pessoa['Ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
# from datetime from datetime as dt
# anoAtual = dt.now()
# data = anoAtual.date()
# ano = data.strftime("%Y")
del pessoa['AnoNascimento']
if pessoa['Ctps'] != 0:
    pessoa['Contratacao'] = int(input('Ano de Contratação: '))
    pessoa['Salario'] = float(input('Salário: '))
    pessoa['Aposentadoria'] = pessoa['Idade'] +((pessoa['Contratacao'] + 35) - anoAtual)
else:
    pessoa['Ctps'] = 0
print('-=' * 30)
for k, v in pessoa.items():
    print(f'- {k} tem o valor {v}')

