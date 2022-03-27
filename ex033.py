a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))
# verificando o menor valor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# verificando o menor valor
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))

# como eu implementei
'''
lista = []
a = int(input('Primeiro número: '))
lista.append(a)
b = int(input('Segundo número: '))
lista.append(b)
c = int(input('Terceiro número: '))
lista.append(c)
print('O menor valor digitado foi {}'.format(min(lista)))
print('O maior valor digitado foi {}'.format(max(lista)))
'''
