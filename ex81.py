lista = list()
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
lista.sort(reverse=True)
print(f'Você digitou {len(lista)} elementos')
print(f'Os valores em ordem decrescente são {lista}')
print('O valor 5 faz parte da lista' if 5 in lista else 'O valor 5 não foi encontrado na lista')
