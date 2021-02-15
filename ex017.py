#Calculo hipotenusa
import math
catop = float(input('Digite o comprimento do cateto oposto:'))
catad = float(input('Digite o comprimento do cateto adjacente'))
hip = math.hypot(catop,catad)
print('O comprimento da hipotenusa é {:.2f}'.format(hip))
