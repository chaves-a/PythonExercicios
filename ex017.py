#import math
from math import hypot
opo = float(input('Comprimento do cateto oposto: '))
adj = float(input('Comprimento do cateto adjacente: '))
print('A hipotenusa vai medir {:.2f}'.format(hypot(opo, adj)))


#outra forma de fazer
'''
opo = float(input('Comprimento do cateto oposto: '))
adj = float(input('Comprimento do cateto adjacente: '))
hip = (opo ** 2 + adj ** 2) ** (1 / 2)
print('A hipotenusa vai medir {:.2f}'.format(hip))
'''