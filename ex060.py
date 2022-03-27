n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))

'''
# como ele implementou primeiro - usou um método do python para calcular fatorial
from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))


# como eu implementei sozinho
número = int(input('Digite um número para calcular seu Fatorial: '))
fatorial = 1
while número != 1:
    fatorial = fatorial * número
    número -= 1
print(fatorial)
'''