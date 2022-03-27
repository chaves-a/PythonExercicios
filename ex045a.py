# forma como eu implementei sozinho (antes da aula)

from random import randint
from time import sleep
print('''Suas opções
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
j = int(input('Qual é a sua jogada? '))
c = randint(0, 2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
if j == 0:
    opj = 'Pedra'
elif j == 1:
    opj = 'Papel'
elif j == 2:
    opj = 'Tesoura'
if c == 0:
    opc = 'Pedra'
elif c == 1:
    opc = 'Papel'
elif c == 2:
    opc = 'Tesoura'
print('-=' * 12)
print('Computador jogou {}'.format(opc))
print('Jogador jogou {}'.format(opj))
print('-=' * 12)
if j == 2 and c == 1 or j == 1 and c == 0 or j == 0 and c == 2:
    print('JOGADOR VENCE')
elif c == 2 and j == 1 or c == 1 and j == 0 or c == 0 and j == 2:
    print('COMPUTADOR VENCE')
else:
    print('EMPATE')
