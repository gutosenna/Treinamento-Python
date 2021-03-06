def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO! \"{entrada}\" é um preço inválido.\033[m')
        else:
            válido = True
            if válido:
                return float(entrada)


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        try:
            if n.isnumeric():
                valor = int(n)
                break
        except:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            continue
    return valor

def leiaFloat(msg):
    pass