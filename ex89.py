# Exercício Python 089:
# Crie um programa que leia nome e duas notas de vários alunos e
# guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e
# permita que o usuário possa mostrar as notas de cada aluno individualmente.
boletim, alunos, notas = list(), list(), list()

while True:
    alunos.append(str(input('Nome: ').capitalize()))
    for n in range(1, 3):
        notas.append(float(input(f'Nota {n}: ')))
    boletim.append(notas[:])
    notas.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('No. Nome  MÉDIA')
for i, al in enumerate(alunos):
    print(i, '  ', alunos[i], '  ', sum(boletim[i])/2)
while True:
    r = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if r == 999:
        print('FINALIZANDO...')
        print('<<< VOLTE SEMPRE >>>')
        break
    elif r <= len(alunos) - 1:
        print('-' * 60)
        print(f'Notas de {alunos[r]} são {boletim[r]}')
        print('-' * 60)
    else:
        print('ALUNO NÃO CADASTRADO! TENTE UM NÚMERO VÁLIDO.')
