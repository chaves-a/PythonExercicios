from random import randint
from time import sleep # chamando o método sleep da biblioteca time
computador = randint(0, 5) # faz o computador "pensar"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2) # para dar a ideia de que o computador está processando
if computador == jogador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
