from time import sleep


def maior(* num):
        print('-=' * 30)
        print('Analisando os valores passados...')
        mai = 0
        for v in num:
            if v > mai:
                mai = v
            print(f'{v} ', end='')
            sleep(0.3)
        print(f'Foram informados {len(num)} valores ao todo.')
        print(f'O maior valor informado foi {mai}.')


# Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
