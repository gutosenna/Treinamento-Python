import numpy as np
from PIL import ImageGrab
from click2 import click, queryMousePosition, PressKey, ReleaseKey, SPACE
import time

tamanhotela = [1315,400,1520,410]
cor = [0,0,0]

def clicanatela(jobu):
 global tamanhotela
 jobu = [i[0] for i in jobu]
 x = int(jobu[1] + tamanhotela[0] +1)
 y = int(jobu[0] + tamanhotela[1] +60)
 click(x,y)
 start_time = 0

while True:
 time.sleep(10)
 start_time = time.time()
 screen = np.array(ImageGrab.grab(bbox=tamanhotela))
 color=np.array(cor,dtype=np.uint8)
 jobu=np.where(np.all((screen==color),axis=-1))
 if len(jobu[0]) > 0:
  clicanatela(jobu)
  cliqueporsegundos =  (time.time() - start_time)
  print("clique por segundo {}".format(cliqueporsegundos))