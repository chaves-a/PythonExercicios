núm = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º. valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)  # adiciona o valor na posição 0 da lista
    else:
        núm[1].append(valor)  # adiciona o valor na posição 1 da lista
print('-=' * 30)
núm[0].sort()  # ordena a lista simples que representa o primeiro elemento da lista composta
núm[1].sort()
print(f'Os valores pares digitados foram: {núm[0]}')
print(f'Os valores ímpares digitados foram: {núm[1]}')



# como eu implementei sozinho... mas sei que o certo era fazer uma lista composta
'''
cont = 1
par = []
impar = []
for c in range(0, 7):
    valor = int(input(f'Digite o {cont}º. valor: '))
    cont += 1
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
par.sort()
impar.sort()
print(f'Os valores pares digitados foram: {par}')
print(f'Os valores ímpares digitados foram: {impar}')
'''
