matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # já declarou a lista composta com as linhas como listas simples dentro da composta
for l in range(0, 3):  # os dois for vão alimentar a matriz - l para linha e c para coluna
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))  # [l] e [c] vão definir a posição que vai entrar o número digitado
print('-=' * 30)
for l in range(0, 3):  # esses dois são para mostrar a estrutura na tela
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()  # esse print nessa posição serve para que toda vez que o último for termine as colunas, ele quebre a linha

