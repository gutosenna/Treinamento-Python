n = contador = soma = 0
while True:
    n = int(input('Digite um número: [999 para encerrar. '))
    if n == 999:
        break
    contador += 1
    soma += n
print(f'Você digitou {contador} números e a soma entre eles é {soma}')

