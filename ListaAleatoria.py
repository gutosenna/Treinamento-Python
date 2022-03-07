from random import random


def listaAleatoria(n):
  s = [0] * n
  for i in range(n):
    s[i] = random()
    print(s)
  return s
listaAleatoria(8)
