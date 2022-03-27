num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram ', end='')
for n in num: # ele esqueceu de tirar o zero
    if n % 2 == 0:
        print(n, end=' ')


# como eu implementei - eu entendi errado a última linha exibida pelo programa - ele pediu para exibir os números pares e não quantas vezes aparecem números pares
'''
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
valores = (n1, n2, n3, n4)
print(f'Você digitou os valores {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes')
print(f'O valor 3 apareceu na {valores.index(3) + 1}ª posição')
cont = 0
for c in valores:
    if c != 0:
        if c % 2 == 0:
            cont += 1
print(f'Os valores pares digitados foram {cont}')
'''