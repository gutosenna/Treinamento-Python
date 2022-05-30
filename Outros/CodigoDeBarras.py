from barcode import EAN13
from barcode.writer import ImageWriter

with open(r'F:\PROGRAMACAO\PYTHON\codigo2.png', 'wb') as f:
    EAN13('8743681185337362', writer=ImageWriter()).write(f)
