matriz = [[], [], []]
for linha in range(3):
        for coluna in range(3):
            matriz[coluna].append(int(input(f'Digite o valor [{linha}][{coluna}]: ')))
for cont in range(3):
    print(f' [{matriz[0][cont]:^5}][{matriz[1][cont]:^5}][{matriz[2][cont]:^5}]')