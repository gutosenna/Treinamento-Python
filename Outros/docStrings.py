def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    :return: sem retorno
    Função criada por Guto
    """
    s = a + b + c
    print(f'A soma vale {s}')

def somar2(*c):
    """
    -> Faz a soma de qualquer valor e mostra o resultado na tela.
    :param c: qualquer valor passados por parametros
    :return: sem retorno
    """
    s = 0
    for v in c:
        s += v
    print(s)


# somar(3, 3)
# somar2(1, 2, 3, 4, 10)

