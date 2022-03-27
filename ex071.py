print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$ '))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R$ {céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')


# como eu implementei sozinho
'''
print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
saque = int(input('Que valor você quer sacar? R$ '))
ced50 = ced20 = ced10 = ced1 = 0
while True:
    while saque >= 50:
        saque -= 50
        ced50 += 1
    while 20 <= saque < 50:
        saque -= 20
        ced20 += 1
    while 10 <= saque < 20:
        saque -= 10
        ced10 += 1
    while 1 <= saque < 10:
        saque -= 1
        ced1 += 1
    if saque == 0:
        break
if ced50 > 0:
    print(f'Total de {ced50} cédulas de R$ 50')
if ced20 > 0:
    print(f'Total de {ced20} cédulas de R$ 20')
if ced10 > 0:
    print(f'Total de {ced10} cédulas de R$ 10')
if ced1 > 0:
    print(f'Total de {ced1} cédulas de R$ 1')
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
'''
