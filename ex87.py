matriz = []
for c in range(3):
        for i in range(3):
            matriz.append(int(input(f'Digite o valor [{c}][{i}]: ')))
for cont in range(9):
    print(f' [{matriz[cont]}]')