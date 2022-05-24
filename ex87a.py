#Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = t_coluna = v_maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}][{c}]: '))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
        #t_coluna = matriz[0][2] + matriz[1][2] + matriz[2][2]
        '''if matriz[1][0] > 0:
            v_maior = matriz[1][0]
        if matriz[1][1] > v_maior:
            v_maior = matriz[1][1]
        if matriz[1][2] > v_maior:
            v_maior = matriz[1][2]'''
print('=-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma de todos os valores pares digitados é {par}')
for l in range(3):
    t_coluna += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {t_coluna}')
for c in range(0, 3):
    if c == 0:
        v_maior = matriz[1][c]
    elif matriz[1][c] > v_maior:
        v_maior = matriz[1][c]
print(f'O maior valor da segunda linha é {v_maior}')