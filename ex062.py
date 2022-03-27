print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print('{} -> '.format(termo), end='')
        termo += razão
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você que mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))


# como eu implementei - cheio de gambiarra, mas foi
'''
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
c = 1
a = 11
while c != 0:
    c += 1
    if c <= a:
        print('{} -> '.format(termo), end='')
        print('PAUSA' if c > (a - 1) else '', end='')
        termo += razão
    else:
        d = int(input('\nQuantos termos você quer mostrar a mais? '))
        if d != 0:
            a = c + d - 1
            print('{} -> '.format(termo), end='')
            print('PAUSA' if c > (a - 1) else '', end='')
            termo += razão
        else:
            c = c - 2
            print('Progressão finalizada com {} termos mostrados.'.format(c))
            break
'''