from datetime import date
trabalhador = dict()
trabalhador['nome'] = str(input('Nome: '))
trabalhador['idade'] = date.today().year - int(input('Ano de Nascimento: '))
trabalhador['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if trabalhador['ctps'] != 0:
    trabalhador['contratação'] = int(input('Ano de Contratação: '))
    trabalhador['salário'] = float(input('Salário: R$ '))
    trabalhador['aposentadoria'] = (trabalhador['idade'] + 35) - (date.today().year - trabalhador['contratação'])
print('-=' * 30)
for k, v in trabalhador.items():
    print(f'  - {k} tem o valor {v}')
