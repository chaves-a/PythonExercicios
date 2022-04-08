pessoa = dict()
galera = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())  # forma de copiar um dicionário para dentro de uma lista
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in galera:  # aqui ele pegou cada elemento da lista - cada um deles é um dicionário
    if p['sexo'] == 'F':  # em seguida, para cada dicionário ele pergunta se a chave sexo é igual a F
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in galera:  #  aqui ele pegou cada elemento da lista - cada um deles é um dicionário
    if p['idade'] >= media:  # em seguida, para cada dicionário ele pergunta se a chave idade é maior ou igual a media
        print('   ', end='')
        for k, v in p.items():  # aqui ele pega cada dicionário que passou pelo if e detalha ele
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
