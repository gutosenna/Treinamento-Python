from datetime import date
ano_nascimento = int(input('Em qual ano você nasceu? '))
ano_atual = date.today().year
resultado = ano_atual - ano_nascimento
if resultado < 18:
    print('Ainda não completou a idade correta, faltam {} anos para se alistar'.format(abs(18 - resultado)))
    ano = ano_atual + resultado
    print('Voce deverá alistar em {}'.format(ano))
elif resultado == 18:
    print('Está na hora de se alistar')
elif resultado > 18:
    print('Já passou da hora de se alistar, vc está atrasado em {} anos'.format(resultado - 18))
    ano = ano_atual - resultado + 18
    print('Voce deveria ter se alistado em {}'.format(ano))