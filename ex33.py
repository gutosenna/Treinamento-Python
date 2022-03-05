numero = int(input('Digite um numero: ')),\
         int(input('Digite o segundo numero: ')), \
         int(input('Digite o terceiro numero: '))
if numero[0] > numero[1] and numero[0] > numero[2]:
    print(f'O numero {numero[0]} é maior')
elif numero[1] > numero[0] and numero[1] > numero[2]:
    print(f'O numero {numero[1]} é maior')
elif numero[2] > numero[1] and numero[2] > numero[0]:
    print(f'O numero {numero[2]} é maior')