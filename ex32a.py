import datetime

ano = int(input('Qual ano deseja analisar? Digite 0 para analisar ano atual: '))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÂO É BISSEXTO'.format(ano))
