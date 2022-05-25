numeros = [[], []]
valor = 0
for i in range(1, 8):
    valor = (int(input(f'Digite o {i}º valor: ')))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
print('=-' * 30)
print(f'Numeros pares {sorted(numeros[0])}')
print(f'Numeros impares {sorted(numeros[1])}')