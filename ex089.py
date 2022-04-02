ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input(('Quer continuar? [S/N] '))).upper().strip()
    if resp in 'N':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print(('FINALIZANDO...'))
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')


# como eu implementei... só não consegui fazer o alinhamento da tabela... mas o certo é salvar tudo em listas e não calcular como eu fiz para a média, por exemplo...
'''
composta = []
simples = []
while True:
    simples.append(str(input('Nome: ')))
    simples.append(float(input('Nota 1: ')))
    simples.append(float(input('Nota 2: ')))
    composta.append(simples[:])
    simples.clear()
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()
    if resp in 'N':
        break
print('-=' * 30)
print('No.  NOME           MÉDIA')
print('-' * 30)
for i, l in enumerate(composta):
    print(f'{i}    {composta[i][0]}', end='')
    print(f'{(composta[i][1] + composta[i][2]) / 2:>16}')
print('-' * 40)
while True:
    mostra = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if mostra == 999:
        break
    else:
        print(f'Notas de {composta[mostra][0]} são [{composta[mostra][1]}, {composta[mostra][2]}]')
    print('-' * 40)
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
'''