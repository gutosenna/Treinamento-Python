# Sorteando um item na lista 02

import random
alu = [input('Digite o nome do primeiro aluno:'), input('O segundo aluno:'), input('Outro:'), input('ultimo:')]
sort = random.choice(alu)
print('O aluno sorteado da vez foi:', sort)