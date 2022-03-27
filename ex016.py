#import math
from math import trunc
num = float(input('Digite um número: '))
#print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))

#outra forma de fazer sem importar nada
#num = float(input('Digite um número: '))
#print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))

