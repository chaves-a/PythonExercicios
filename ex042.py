a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a + b > c and a + c > b and b + c > a:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if a == b == c:
        print('equilátero.')
    elif a != b != c != a:
        print('escaleno')
    else:
        print('isósceles')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
