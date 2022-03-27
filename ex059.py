from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opção = int(input('>>>>> Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')


# como eu implementei
'''
primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))
print('     [ 1 ] somar')
print('     [ 2 ] multiplicar')
print('     [ 3 ] maior')
print('     [ 4 ] novos números')
print('     [ 5 ] sair do programa')
c = False
while not c:
    opção = int(input('>>>>> Qual é a sua opção? '))
    if opção == 1:
        print('A soma entre {} + {} é {}'.format(primeiro, segundo, primeiro + segundo))
    if opção == 2:
        print('O resultado de {} x {} é {}'.format(primeiro, segundo, primeiro * segundo))
    if opção == 3:
        if primeiro > segundo:
            print('Entre {} e {} o maior é {}'.format(primeiro, segundo, primeiro))
        elif primeiro < segundo:
            print('Entre {} e {} o maior é {}'.format(primeiro, segundo, segundo))
        else:
            print('Os valores são iguais')
    if opção == 4:
        primeiro = int(input('Primeiro valor: '))
        segundo = int(input('Segundo valor: '))
    if opção == 5:
        c = True
    if opção not in [1, 2, 3, 4, 5]:
        print('Opção inválida. Tente novamente')
print('Fim do programa! Volte sempre!')
'''
