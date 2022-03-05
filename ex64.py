cont = soma = 0
num = int(input('Digite um número: [999 para encerrar]. '))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um número: [999 para encerrar]. '))
print('Vc digitou {} números e a soma deles é {}'.format(cont, soma))
