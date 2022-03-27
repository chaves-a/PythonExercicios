somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('----- {}ª PESSOA ----- '.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
médiaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(médiaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))


# como eu implementei sozinho primeiro:
'''
somaidades = 0
velho = 0
homem = ''
sexo = ''
mulher = 0
for p in range(1, 5):
    print('-' * 4, ' {}ª PESSOA '.format(p), '-' * 4)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    somaidades += idade
    if p == 1:
        velho = idade
        if sexo == 'M':
            homem = nome
    else:
        if sexo == 'M':
            if idade > velho:
                velho = idade
                homem = nome
    if sexo == 'F':
        if idade < 20:
            mulher += 1
print('A média de idade do grupo é de {:.1f} anos'.format(somaidades / 4))
print('O homem mais velho tem {} anos e se chama {}.'.format(velho, homem))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulher))
'''