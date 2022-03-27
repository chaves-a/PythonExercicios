valores = []
while True:
    num = int(input('Digite um valor: '))
    if num in valores:
        print('Valor duplicado! Não vou adicionar...')
    else:
        valores.append(num)
        print('Valor adicionado com sucesso...')
    decisão = str(input('Quer continuar? [S/N] ')).strip().upper()
    if decisão in 'N':
        break
print('-=' * 30)
valores.sort()
print(f'Você digitou os valores {valores}')
