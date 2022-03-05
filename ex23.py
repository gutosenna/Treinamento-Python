número = int(input('Informe um número: '))
print('Analisando o número {}'.format(número))
unidade = número // 1 % 10
dezena = número // 10 % 10
centena = número // 100 % 10
milhar = número // 1000 % 10
print(f'Unidade: {unidade}\n Dezena: {dezena} \n Centena: {centena} \n Milhar {milhar}')

'''número = str(input('Informe um número: '))
print('Analisando o número {}'.format(número))
print(f'Unidade: {número[3]}\n Dezena: {número[2]} \n Centena: {número[1]} \n Milhar {número[0]}')'''
