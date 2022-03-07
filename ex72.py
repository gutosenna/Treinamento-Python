while True:
    numero = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro',
              'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
              'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze',
              'Quinze', 'Desesseis', 'Dezessete', 'Dezoito',
              'Dezenove', 'Vinte')
    while True:
        n = int(input('Digite um número entre 0 e 20: 999 para encerrar.'))
        if 0 <= n <= 20 or n == 999:
            break
        print('Tente novamente. ', end='')
    if n == 999:
        break
    print(f'Voce digitou o número {numero[n]}')
print('Programa encerrado!')

