from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI': # esse laço garante que a pessoa precisa digitar P ou I - se ele digitar outra letra vai repetir a pergunta
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR') # estrutura condicional em uma linha só - ele chamou de "o clássico operador ternário"
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PEDREU')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PEDREU')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')


# como eu implementei
'''
from random import randint
cont = 0
print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)
while True:
    c = randint(0, 10)
    j = int(input('Digite um valor: '))
    pi = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    s = j + c
    if s % 2 == 0:
        r = 'PAR'
    else:
        r = 'ÍMPAR'
    print('-' * 30)
    print(f'Você jogou {j} e o computador {c}. Total de {s} DEU {r}')
    print('-' * 30)
    if (r == 'PAR' and pi == 'I') or (r == 'ÍMPAR' and pi == 'P'):
        print('Você PERDEU!')
        print('=-' * 15)
        break
    if (r == 'PAR' and pi == 'P') or (r == 'ÍMPAR' and pi == 'I'):
        cont += 1
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('=-' * 15)
print(f'GAME OVER! Você venceu {cont} vezes.')
'''