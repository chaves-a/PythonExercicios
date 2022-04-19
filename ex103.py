def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


# Programa Principal
print('-' * 20)
n = str(input('Nome do Jogaor: '))
g = str(input('Número de Gols: '))  # colocou como string pois aí ele deixa preencher vazio sem dar erro
if g.isnumeric():  # uso isso para realmente ver se o que foi digitado é um número
    g = int(g)
else:
    g = 0
if n.strip() == '':  # nesse if eu passo só o parâmetro de gols se o nome for vazio - e no else eu passo os dois parâmetros
    ficha(gol=g)
else:
    ficha(n, g)
