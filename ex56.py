idadeMaior = 0
soma = 0
mulher = 0
homemMaisVelho = ''
media = 0
for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma += idade
    media = soma / c
    if c == 1 and sexo in 'Mm':
        idadeMaior = idade
        homemMaisVelho = nome
    else:
        if idade > idadeMaior and sexo in 'Mm':
            idadeMaior = idade
            homemMaisVelho = nome
        if sexo in 'Ff' and idade < 21:
            mulher += 1
print('O homem mais velho tem {} anos e se chama {}'.format(idadeMaior, homemMaisVelho))
print('A média das idade é {}'.format(media))
print('Ao todo são {} mulheres com menos de 21 anos'.format(mulher))
