import datetime

maior = 0
menor = 0
anoAtual = datetime.date.today().year
for c in range(1, 8):
    pessoa = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    total = anoAtual - pessoa
    if total < 18:
        menor += 1
    elif total >= 18:
        maior += 1
print('Existem {} pessoas menor de idade'.format(menor))
print('Existem {} pessoas maior de idade'.format(maior))