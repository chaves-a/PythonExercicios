from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))


# como eu implementei sozinho primeiro
'''
from datetime import date
atual = date.today().year
cont = 0 # não precisava ter criado esse contador pois bastava usar a variável "x" do próprio for
maior = 0
menor = 0
for x in range(1, 8):
    cont += 1 # não precisava ter criado esse contador pois bastava usar a variável "x" do próprio for
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(cont))) # não precisava ter criado esse contador pois bastava usar a variável "x" do próprio for
    if atual - nasc >= 21:
        maior += 1
    else:
        menor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
print('E também tivemos {} pessoas menores de idade'.format(menor))
'''
