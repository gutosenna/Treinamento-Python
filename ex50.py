s = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {}° Número: '.format(c)))
    if n % 2 == 0:
        s += n
        cont += 1
print('Você informou {} número PARES, e a soma entre os números eles é {}'.format(cont, s))