resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
media = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))


# como eu implementei
'''
número = contador = soma = maior = menor = 0
continuar = 'S'
while continuar == 'S':
    número = int(input('Digite um número: '))
    contador += 1
    soma += número
    if número > maior:
        maior = número
    else:
        menor = número
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
print('Você digitou {} números e a média foi {:.2f}'.format(contador, soma / contador))
print('O maior valor foi {} e o menor foi {}'.format(maior, número))
'''
