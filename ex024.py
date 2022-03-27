# como ele implementou:
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')
# o dele é o correto pois ele pergunta se o nome da cidade COMEÇA com a palavra Santo.

# como eu implementei:
#cidade = str(input('Em que cidade você nasceu? ')).lower()
#print('santo' in cidade)
# na minha forma ele vai achar Santo em qualquer posição