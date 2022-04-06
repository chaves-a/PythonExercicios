from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)  # método para ordenar um dicionário - o itemgetter(1) ordena pelo valor - se usar 0 ele vai ordenar pela chave - observar que ele gera uma lista e não um dicionário
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'   {i + 1}º lugar: {v[0]} com {v[1]}')
    sleep(1)


# como eu implementei - acho que a minha solução foi melhor - eu consultei o método na internet
'''
from random import randint
from time import sleep
c = 1
resultados = {}
for j in range(1, 5):
    sorteio = randint(1, 6)
    resultados[f'jogador{j}'] = sorteio
for k, v in resultados.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')
for i in sorted(resultados, key=resultados.get, reverse=True):  # método para ordenar um dicionário com base nos valores - a parte final - reverse=True - faz ficar na ordem decrescente
    print(f'   {c}º lugar: {i} com {resultados[i]}')
    c += 1
    sleep(1)
'''