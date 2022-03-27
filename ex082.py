num = list()
pares = list()
ímpares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)
print('-=' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {ímpares}')
print('Nova linha inserida e commit feito direto do PyCharm')

# como eu implementei sozinho
'''
completa = []
par = []
ímpar = []
while True:
    n = int(input('Digite um número: '))
    completa.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        ímpar.append(n)
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp in 'N':
        break
print('-=' * 30)
print(f'A lista completa é {completa}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {ímpar}')
'''