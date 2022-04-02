from random import randint
from time import sleep
lista = list()
jogos = list()
print('-' * 30)
print('   JOGAR NA MEGA SENA   ')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' *  3, f' SORTEANDO {quant} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)


# como eu tentei implementar... mas não deu certo...
'''
from random import randint
jogo = []
titulo = 'JOGAR NA MEGA SENA'
print('-' * 30)
print(f'{titulo:^30}')
print(('-' * 30))
sorteios = int(input('Quantos jogos você quer que eu sorteie? '))
print('-=' * 3, end='')
print(f'  SORTEANDO 5 JOGOS   ', end='')
print('-=' * 3)
for j in range(1, sorteios + 1):
    for n in range(0, 6):
        if n == 0:
            jogo.append(randint(1, 60))
        else:
            aleat = randint(1, 60)
            if aleat not in jogo:
                jogo.append(aleat)
            else:
                n -= 1
    jogo.sort()
    print(f'Jogo {j}: {jogo}')
    jogo.clear()
'''