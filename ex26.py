frase = str(input('Digite uma frase: ')).strip()
print(f'''A letra A apareceu {frase.upper().count('A')} vezes na frase
A primeira letra A apareceu na posição {frase.upper().find('A')+1}
A última letra A apareceu na posição {frase.upper().rfind('A')+1}''')
