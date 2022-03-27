print('-' * 30)
print('{:^30}'.format('LOJA SUPER BARATÃO'))
print('-' * 30)
cont = total = prodMaisMil = menorPreço = 0
prodMaisBarato = ' '
while True:
    produto = str(input('Nome do Produto: ')).strip()
    preço = float(input('Preço: R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        prodMaisMil += 1
    if cont == 1 or preço < menorPreço:
        prodMaisBarato = produto
        menorPreço = preço
    decisão = ' '
    while decisão not in "SN":
        decisão = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if decisão in 'N':
        break
print('{:-^35}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {prodMaisMil} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {prodMaisBarato} que custa R$ {menorPreço:.2f}')
