num = contador = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    contador += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(contador, soma))


# como eu implementei
'''
num = int(input('Digite um número [999 para parar]: '))
contador = 0
soma = num
while num != 999:
    contador += 1
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:
        soma += num
    else:
        soma = soma
print('Você digitou {} números e a soma entre eles foi {}.'.format(contador, soma))
'''