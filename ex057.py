# como ele implementou
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0] #tirando os espaços, jogando para maiúsculo e pegando apenas a primeira letra
while sexo not in 'MmFf': # com o upper nem precisava testar os minúsculos
        sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))


# como eu implementei
'''
sexo = str(input('Informe seu sexo: [M/F] '))upper()
while sexo != 'M' and sexo != 'F':
        sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).upper()
print('Sexo {} registrado com sucesso'.format(sexo))
'''