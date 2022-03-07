import random

cont = 0
maior = menor = ()
for c in range(0, 10):
    tupla = (random.randint(0, 10))
    print(tupla, end=' ')
    cont += 1
    if cont == 1:
        maior = menor = tupla
    else:
        if tupla < menor:
            menor = tupla
        elif tupla > maior:
            maior = tupla
print(f'\nO maior é {maior} e o menor é {menor}')
print('Fim do programa')
