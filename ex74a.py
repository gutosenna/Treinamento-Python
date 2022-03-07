import random

tupla = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10))
print(tupla, end=' ')
print(f'\nO maior é {max(tupla)} e o menor é {min(tupla)}')