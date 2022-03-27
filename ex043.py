peso = float(input('Informe seu peso (em kg): '))
altura = float(input('Informe sua altura (em metros): '))
imc = peso / (altura ** 2)
print('Seu IMC é {:.1f} e você está '.format(imc), end='')
if imc < 18.5:
    print('abaixo do peso.')
elif 18.5 <= imc < 25:
    print('no peso ideal')
elif 25 <= imc < 30:
    print('com sobrepeso')
elif 30 <= imc < 40:
    print('com obesidade')
else:
    print(('obesidade mórbida'))
