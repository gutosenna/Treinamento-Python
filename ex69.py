maiores = homens = mulheres = 0
while True:
    print('-' * 30)
    print('\tCADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).strip()
    if idade >= 18:
        maiores += 1
    if sexo in 'Mm':
        homens += 1
    if sexo in 'Ff' and idade < 20:
        mulheres += 1
    else:
        if idade != type(idade) or sexo != type(sexo):
            print('Errado')
    print('-' * 30)
    opcao = str(input('Quer continuar? [S/N] ')).strip()
    if opcao in 'Ss':
        continue
    else:
        break
print('Total de pessoas com mais de 18 anos: {}'.format(maiores))
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres} mulheres com menos de 20 anos')



