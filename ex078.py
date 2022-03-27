listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=-' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}... ', end='')
print()


# como eu implementei
'''
valores = list()
cont = 0
for c in range(0, 5):
    num = int(input(f'Digite um valor para a Posição {cont}: '))
    cont += 1
    valores.append(num)
print('=-' * 25)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições ', end='')
posmax = 0
for p in valores:
    if max(valores) == p:
        print(f'{posmax}... ', end='')
    posmax += 1
print(f'\nO menor valor digitado foi {min(valores)} nas posições ', end='')
posmin = 0
for p in valores:
    if min(valores) == p:
        print(f'{posmin}... ', end='')
    posmin += 1
'''