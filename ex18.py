# Exercício Python 18: Seno, Cosseno e Tangente
# Faça um programa que leia um ângulo qualquer e
# mostre na tela o valor do seno,
# cosseno e tangente desse ângulo.
import math
angulo = float(input('Digite o ângulo desejado: '))
print('SENO = {:.2f}'.format(math.sin(math.radians(angulo))))
print('COSENO = {:.2f}'.format(math.cos(math.radians(angulo))))
print('TANGENTE = {:.2f}'.format(math.tan(math.radians(angulo))))