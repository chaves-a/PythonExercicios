dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
pagar = 60 * dias + 0.15 * km
print('O total a pagar é de R$ {:.2f}'.format(pagar))
