cont = 0
soma = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        soma += n
        cont += 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))


# para conferir se está gerando os números certos

'''
for n in range(1, 501, 2):
    if n % 3 == 0:
        print(n, end=' ')
'''