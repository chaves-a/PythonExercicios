tabela = ('FLAMENGO', 'SANTOS', 'PALMEIRAS', 'GRÊMIO',
          'ATHLETICO', 'SÃO PAULO', 'INTERNACIONAL',
          'CORINTHIANS', 'FORTALEZA', 'GOIÁS', 'BAHIA',
          'VASCO', 'ATLÉTICO-MG', 'FLUMINENSE', 'BOTAFOGO',
          'CEARÁ', 'CRUZEIRO', 'CSA', 'CHAPECOENSE', 'AVAÍ')
print('-=' * 20)
print(f'Lista de times do Brasileirão: {tabela}')
print('-=' * 20)
print(f'Os 5 primeiros são {tabela[0:5]}')
print('-=' * 20)
print(f'Os 4 últimos são {tabela[-4:]}')
print('-=' * 20)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print('-=' * 20)
print(f'A Chapecoense está na {tabela.index("CHAPECOENSE") + 1}ª posição') # se usar aspas simples na busca por Chapecoense ele vai dar erro pois teria aspas simples dentro de aspas simples - posso usar aspas duplas ou fazer o .format
