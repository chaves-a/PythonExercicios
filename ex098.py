from time import sleep


def contador (i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1.5)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
        print('FIM!')


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)


# Como eu implementei
'''
from time import sleep


def contador(início, fim, passo):
    print('-=' * 30)
    print(f'Contagem de {início} até {fim} de {passo} em {passo}')
    for v in range(início, fim + passo, passo):
        print(f'{v} ', end='')
        sleep(0.5)
    print('FIM!')


# Programa principal
contador(1, 10, 1)
contador(10, -0, -2)
print('-=' * 30)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
if i > f:
    if p > 0:
        p *= -1
contador(i, f, p)
'''