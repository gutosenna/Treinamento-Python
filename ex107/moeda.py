def aumentar(n, taxa):
    aumentado = n + (n * (taxa/100))
    print(f'Aumentando 10%, temos {aumentado}')


def diminuir(n, taxa):
    diminuido = n - (n * (taxa / 100))
    print(f'Diminuindo 10%, temos {diminuido}')


def dobro(n):
    print(f'O dobro de {n} é {n * 2}')


def metade(n):
    print(f'A metade de {n} é {n / 2}')
