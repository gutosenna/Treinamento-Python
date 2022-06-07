def aumentar(n=0, taxa=0, formatado=False):
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
