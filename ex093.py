jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'   Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)  #forma de somar os valores de uma chave
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')  # pegou o total de partidas pelo tamanho da lista contida na chave gols
for i, v in enumerate(jogador['gols']):  # o for usando enumerate e a chave gols
    print(f'   => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')


# como eu implementei
'''
aprov = {}
listagols = []
total = 0
ranking = []
aprov['nome'] = str(input('Nome do Jogador: '))
qtd = int(input(f'Quantas partidas {aprov["nome"]} jogou? '))
for c in range(1, qtd + 1):
    gol = int(input(f'   Quantos gols na partida {c}? '))
    listagols.append(gol)
    total += gol
aprov['gols'] = listagols
aprov['total'] = total
print('-=' * 30)
print(aprov)
print('-=' * 30)
for k, v in aprov.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {aprov["nome"]} jogou {qtd} partidas.')
for p, g in enumerate(listagols):
    print(f'   => Na partida {p + 1}, fez {g} gols.')
print(f'Foi um total de {total} gols.')
'''