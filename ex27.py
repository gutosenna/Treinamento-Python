nome_completo = str(input('Digite seu nome completo: ')).strip()
print('Muito prazer em te conhecer!')
nome = nome_completo.split()
print(f'Seu primeiro nome é: {nome[0]}\n Seu último nome é: {nome[len(nome)-1]}')