s = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        contador += 1
print('A soma entre os {} números são {}'.format(contador,s))