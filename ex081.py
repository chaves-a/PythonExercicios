lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp in 'N':
        break
print('-=' * 30)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print(f'O valor 5 faz parte da lista!')
else:
    print(f'O valor 5 não foi encontrado na lista!')
