def voto(ano):
    from datetime import date  # nesse caso a importação só serve pra dentro da função - isso economiza memória - a classe date só vai ficar na memória durante a execução dessa função e não fora
    hoje = date.today().year
    idade = hoje - ano
    if 18 <= idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    elif idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL.'


print('-' * 20)
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
