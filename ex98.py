from time import sleep

def contador():
    print('-=' * 30)
    print('Contagem de 1 até 10 de 1 em 1')
    for i in range(1, 11):
        print(i, end=' ')
        # sleep(0.3)
    print('FIM!')
    print('-=' * 30)
    # sleep(0.3)
    print('Contagem de 10 até 0 de 2 em 2')
    for i in range(10, -1, -2):
        print(i, end=' ')
        # sleep(0.3)
    print('FIM!')
    print('-=' * 30)
    print('Agora é sua vez de personalizar a contagem!')
    passo()

def passo():
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    if inicio > fim:
        fim = fim - 1
        passo = -passo
        if passo == 0:
            passo = -1
        # if passo < 0:
        #     passo = passo
    if passo == 0:
        passo = 1
    for i in range(inicio, fim, passo):
        print(i, end=' ')
        # sleep(0.3)
    print('FIM!')


contador()
