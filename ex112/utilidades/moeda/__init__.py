def aumentar(n=0, taxa=0, formatado=False):
    """
    -> Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param n: o preço que se quer reajustar.
    :param taxa: qual é a porcentagem do aumento
    :param formatado: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formato.
    """
    resp = n + (n * (taxa / 100))
    return resp if formatado is False else moeda(resp)


def diminuir(n=0, taxa=0, formatado=False):
    resp = n - (n * (taxa / 100))
    if formatado:
        return moeda(resp)
    else:
        return resp


def dobro(n=0, formatado=False):
    resp = n * 2
    return resp if not formatado else moeda(resp)


def metade(n=0, formatado=False):
    resp = n / 2
    if formatado:
        return moeda(resp)
    else:
        return resp


def moeda(n=0.0, moeda='R$'):
    return f'{moeda}{n:>.2f}'.replace('.', ',')


def resumo(n=0, t1=1, t2=1):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado:\t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço:\t{metade(n, True)}')
    print(f'{t1}% de aumento:\t\t{aumentar(n, t1, True)}')
    print(f'{t2}% de redução:\t\t{diminuir(n, t2, True)}')
    print('-' * 30)
