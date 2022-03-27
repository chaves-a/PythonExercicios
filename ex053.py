frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')


# outra forma que ele implementou sem usar o for:
'''
frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1] # usou técnica de fatiamento para inverter a string
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
'''


# como eu implementei sozinho primeiro:
'''
frase = str(input('Digite uma frase: ')).upper().strip().split()
junto = ''.join(frase)
invertido = ''.join(reversed(junto))
print('O inverso de {} é {}'.format(junto, invertido))
if junto != invertido:
    print('A frase digitada não é um palíndromo!')
else:
    print('Temos um palíndromo')
'''