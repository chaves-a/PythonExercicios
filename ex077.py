palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso',
            'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado',
            'programador', 'futuro')
for p in palavras: # o primeiro for pega cada palavra da tupla
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p: # o segundo for trata a palavra como uma lista e verifica letra a letra se ela está entre as vogais
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
