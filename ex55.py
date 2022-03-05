pesoMenor = 0
pesoMaior = 0
for pess in range(1, 7):
    peso = float(input('Peso da {}ª pessoa: '.format(pess)))
    if pess == 1:
        pesoMaior = peso
        pesoMenor = peso
    else:
        if peso > pesoMaior:
            pesoMaior = peso
        if peso < pesoMenor:
            pesoMenor = peso
print('O maior peso entre as 6 pessoas é {}Kg'.format(pesoMaior))
print('O peso menor é {}'.format(pesoMenor))

