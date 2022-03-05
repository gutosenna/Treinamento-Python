import math
# cateto_oposto = int(input("Digite o Cateto oposto: "))
# cateto_adjacente = int(input("Digite o Cateto adjacente: "))
# hipotenusa = (cateto_adjacente**2 + cateto_oposto**2) **(1/2)
# print("A hipotenusa é: {}".format(hipotenusa))
cateto_oposto = float(input("Digite o Cateto oposto: "))
cateto_adjacente = float(input("Digite o Cateto adjacente: "))
hipotenusa = math.hypot(cateto_oposto,cateto_adjacente)
print("A hipotenusa é: {:.2f}".format(hipotenusa))

