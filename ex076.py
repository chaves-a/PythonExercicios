lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
         'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
         'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(lista)):
    if pos % 2 == 0: # os produtos estão na posição par
        print(f'{lista[pos]:.<30}', end='') # trinta posições com alinhamento a esquerda e pontinhos para completar
    else:
        print(f'R${lista[pos]:>7.2f}') # sete posições com alinhamento a direita e o .2f é para que os números tenham duas casas depois da vírgula
print('-' * 40)
