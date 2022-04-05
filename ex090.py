aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-=' * 30)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')



# como eu implementei
'''
dicionario = {}
dicionario['nome'] = str(input('Nome: '))
dicionario['media'] = float(input(f'Média de {dicionario["nome"]}: '))
if dicionario['media'] < 5:
    dicionario['situação'] = 'Reprovado'
elif dicionario['media'] >= 7:
    dicionario['situação'] = 'Aprovado'
else:
    dicionario['situação'] = 'Recuperação'

print('-=' * 30)
print(f' - nome é igual a {dicionario["nome"]}')
print(f' - média é igual a {dicionario["media"]}')
print(f' - situação é igual a {dicionario["situação"]}')

print('-=' * 30)
for k, v in dicionario.items():
    print(f' - {k} é igual a {v}')
'''